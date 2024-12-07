package com.kucoin.universal.sdk.plugin.util;

import com.kucoin.universal.sdk.plugin.model.Meta;
import io.swagger.v3.oas.models.Operation;

import java.util.Map;

/**
 * @author isaac.tang
 */
public class SpecificationUtil {
    public static String EXTENSION_MODEL_META_KEY = "x-meta";

    public static Meta getMeta(Map<String, Object> extension) {
        if (extension == null) {
            return null;
        }
        return (Meta) extension.get(EXTENSION_MODEL_META_KEY);
    }

    public static Meta getMeta(Operation operation) {
        if (operation == null) {
            return null;
        }
        return getMeta(operation.getExtensions());
    }
}
