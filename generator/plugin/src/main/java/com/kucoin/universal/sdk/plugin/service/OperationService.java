package com.kucoin.universal.sdk.plugin.service;

import com.kucoin.universal.sdk.plugin.model.Meta;

import java.util.Map;

/**
 * OperationService is a service used to parse and generate operation information within OpenAPI objects.
 *
 * @author isaac.tang
 */
public interface OperationService {

    /**
     * Update the OpenAPI object and refresh the corresponding operation information.
     */
    void parseOperation();


    /**
     * Return the meta information of the model based on its name.
     *
     * @param operationName the operation name
     * @return the operation meta
     */
    Meta getMeta(String operationName);


    /**
     * Return all service meta
     *
     * @return all service meta
     */
    Map<String, Meta> getServiceMeta();
}
