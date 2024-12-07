package com.kucoin.universal.sdk.plugin.model;

import io.swagger.v3.oas.models.PathItem;

import java.util.HashMap;
import java.util.Map;

public class Meta extends HashMap<String, Object> {

    public Meta(PathItem.HttpMethod httpMethod, String domain, String service, String subService, String method, String methodServiceFmt, boolean privateChannel, boolean webSocket, TopicMeta topicMeta, boolean broker) {
        this.put("httpMethod", httpMethod);
        this.put("domain", domain);
        this.put("service", service);
        this.put("subService", subService);
        this.put("method", method);
        this.put("methodServiceFmt", methodServiceFmt);
        this.put("privateChannel", privateChannel);
        this.put("webSocket", webSocket);
        this.put("otherProperties", topicMeta);
        this.put("broker", broker);
    }

    public PathItem.HttpMethod getHttpMethod() {
        return (PathItem.HttpMethod) this.get("httpMethod");
    }

    public void setHttpMethod(PathItem.HttpMethod httpMethod) {
        this.put("httpMethod", httpMethod);
    }

    public String getDomain() {
        return (String) this.get("domain");
    }

    public void setDomain(String domain) {
        this.put("domain", domain);
    }

    public String getService() {
        return (String) this.get("service");
    }

    public void setService(String service) {
        this.put("service", service);
    }

    public String getSubService() {
        return (String) this.get("subService");
    }

    public void setSubService(String subService) {
        this.put("subService", subService);
    }

    public String getMethod() {
        return (String) this.get("method");
    }

    public void setMethod(String method) {
        this.put("method", method);
    }

    public boolean isPrivateChannel() {
        return (boolean) this.get("privateChannel");
    }

    public void setPrivateChannel(boolean privateChannel) {
        this.put("privateChannel", privateChannel);
    }

    public boolean isWebSocket() {
        return (boolean) this.get("webSocket");
    }

    public void setWebSocket(boolean webSocket) {
        this.put("webSocket", webSocket);
    }

    public TopicMeta getOtherProperties() {
        return (TopicMeta) this.get("otherProperties");
    }

    public void setOtherProperties(Map<String, Object> otherProperties) {
        this.put("otherProperties", otherProperties);
    }

    public String getMethodServiceFmt() {
        return (String) this.get("methodServiceFmt");
    }

    public void setMethodServiceFmt(String methodServiceFmt) {
        this.put("methodServiceFmt", methodServiceFmt);
    }

    public String uniqueServiceName() {
        return getSubService();
    }

    public boolean isBroker() {
        return (boolean) this.get("broker");
    }

    public void setBroker(boolean broker) {
        this.put("broker", broker);
    }
}
