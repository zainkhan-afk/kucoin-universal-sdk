package com.kucoin.universal.sdk.plugin.service;

/**
 * @author isaac.tang
 */
public interface NameService {

    String formatParamName(String name);

    String formatMethodName(String name);

    String formatService(String name);

    String formatPackage(String name);

}
