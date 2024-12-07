package com.kucoin.universal.sdk.plugin.model;

import java.util.HashMap;

/**
 * @author isaac.tang
 */
public class EnumEntry extends HashMap<String, Object> {

    public EnumEntry(String name, String value, Object originalValue, String description, boolean isString) {
        this.put("name", name);
        this.put("value", value);
        this.put("originalValue", originalValue);
        this.put("description", description);
        this.put("isString", isString);
    }

    public String getName() {
        return (String) this.get("name");
    }

    public String getValue() {
        return (String) this.get("value");
    }

    public String getDescription() {
        return (String) this.get("description");
    }

    public void setName(String name) {
        this.put("name", name);
    }

    public void setValue(String value) {
        this.put("value", value);
    }

    public void setDescription(String description) {
        this.put("description", description);
    }

    public void setOriginalValue(Object originalValue) {
        this.put("originalValue", originalValue);
    }

    public Object getOriginalValue() {
        return this.get("originalValue");
    }

    public boolean isString() {
        return (boolean)this.get("isString");
    }

    public void setIsString(boolean isString) {
        this.put("isString", isString);
    }
}
