package com.kucoin.universal.sdk.plugin.service;

import com.kucoin.universal.sdk.plugin.model.Meta;

/**
 * SchemaService is a service used to parse and generate model information within OpenAPI objects.
 *
 * @author isaac.tang
 */
public interface SchemaService {

    /**
     * Update the OpenAPI object and refresh the corresponding model information.
     */
    void parseSchema();


    /**
     * Return the meta information of the model based on its name.
     * If the object is not a request or response of an operation, it may be null.
     *
     * @param modelName the model name
     * @return the meta associated with the model.
     */
    Meta getMeta(String modelName);


    /**
     * Get the generated name based on the model name.
     *
     * @param modelName the model name
     * @return the generated name
     */
    String getGeneratedModelName(String modelName);


}
