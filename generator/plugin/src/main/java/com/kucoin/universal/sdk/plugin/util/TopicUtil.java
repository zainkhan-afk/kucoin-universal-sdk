package com.kucoin.universal.sdk.plugin.util;

import com.kucoin.universal.sdk.plugin.model.TopicMeta;
import com.kucoin.universal.sdk.plugin.service.NameService;
import org.apache.commons.lang3.StringUtils;

import java.util.*;

/**
 * @author isaac.tang
 */
public class TopicUtil {

    private static String[] trimParam(NameService nameService, String param) {
        if (param.startsWith("{") && param.endsWith("}")) {
            param = param.substring(1, param.length() - 1);
        } else {
            throw new RuntimeException("unsupported param" + param);
        }

        List<String> result = new ArrayList<>();
        if (param.contains("_")) {
            for (String s : param.split("_")) {
                s = s.replace("{", "");
                s = s.replace("}", "");

                s = nameService.formatParamName(s);
                result.add(s);
            }
            return result.toArray(new String[0]);
        }
        return new String[]{nameService.formatParamName(param)};
    }

    public static TopicMeta parseTopic(NameService nameService, String topic) {
        if (StringUtils.isEmpty(topic)) {
            throw new RuntimeException("empty topic");
        }

        TopicMeta topicMeta = new TopicMeta();

        // 1. /market/candles:{symbol}_{type}
        // 2. /market/ticker:{symbol},{symbol}
        // 3. /contractMarket/tickerV2:{symbol}
        // 4. /spotMarket/tradeOrders
        // 5. /market/ticker:all
        TopicMeta.Paras parameter = new TopicMeta.Paras();
        if (topic.contains(":")) {
            String[] topicParts = topic.split(":");

            if (!topicParts[1].contains("{") & !topicParts[1].contains("}")) {
                // case 5
                topicMeta.setTopic(topic);
                parameter.setType(Map.of("none", true));
            } else {
                topicMeta.setTopic(topicParts[0]);

                // case 2
                if (topicParts[1].contains(",")) {
                    // {symbol} {symbol}
                    String[] parts = topicParts[1].split(",");

                    if (parts.length == 1) {
                        throw new RuntimeException("not supported topic" + topic);
                    } else {
                        Set<String> s = new HashSet<>(List.of(parts));
                        if (s.size() == 1) {
                            parameter.setType(Map.of("array", true));
                            parameter.setParas(trimParam(nameService, parts[0])[0]);
                        } else {
                            throw new RuntimeException("not supported topic" + topic);
                        }
                    }
                } else if (topicParts[1].contains("_")) {
                    // case 1

                    // {symbol} {type}
                    String[] parts = topicParts[1].split("_");
                    if (parts.length == 1) {
                        throw new RuntimeException("not supported topic" + topic);
                    } else {
                        parameter.setType(Map.of("object", true));
                        parameter.setParas(trimParam(nameService, topicParts[1]));
                    }

                } else {
                    // case 3
                    parameter.setType(Map.of("simple", true));
                    parameter.setParas(trimParam(nameService, topicParts[1])[0]);
                }
            }
        } else {
            // case 4
            topicMeta.setTopic(topic);
            parameter.setType(Map.of("none", true));
        }

        topicMeta.setParas(parameter);

        return topicMeta;
    }
}
