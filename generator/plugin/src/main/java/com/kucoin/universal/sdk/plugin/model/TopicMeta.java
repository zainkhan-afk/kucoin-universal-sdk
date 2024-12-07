package com.kucoin.universal.sdk.plugin.model;

/**
 * @author isaac.tang
 */

import java.util.HashMap;

public class TopicMeta extends HashMap<String, Object> {

    public static class Paras extends HashMap<String, Object> {

        private static final String TYPE_KEY = "type";
        private static final String PARAS_KEY = "paras";

        public Paras() {
            super();
        }

        public Paras(String type, Object paras) {
            this.put(TYPE_KEY, type);
            this.put(PARAS_KEY, paras);
        }

        // Getters
        public Object getType() {
            return this.get(TYPE_KEY);
        }

        public Object getParas() {
            return this.get(PARAS_KEY);
        }

        // Setters
        public void setType(Object type) {
            this.put(TYPE_KEY, type);
        }

        public void setParas(Object paras) {
            this.put(PARAS_KEY, paras);
        }

        // toString method
        @Override
        public String toString() {
            return "Paras{" +
                    "type='" + getType() + '\'' +
                    ", paras=" + getParas() +
                    '}';
        }
    }


    private static final String PARAS_KEY = "parameters";
    private static final String TOPIC_KEY = "topic";

    public TopicMeta() {
        super();
    }

    public TopicMeta(Object paras, String topic) {
        this.put(PARAS_KEY, paras);
        this.put(TOPIC_KEY, topic);
    }

    // Getters
    public Paras getParas() {
        return (Paras)this.get(PARAS_KEY);
    }

    public String getTopic() {
        return (String) this.get(TOPIC_KEY);
    }

    // Setters
    public void setParas(Paras paras) {
        this.put(PARAS_KEY, paras);
    }

    public void setTopic(String topic) {
        this.put(TOPIC_KEY, topic);
    }

    // toString method
    @Override
    public String toString() {
        return "Message{" +
                ", paras=" + getParas() +
                ", topic='" + getTopic() + '\'' +
                '}';
    }
}
