package com.kucoin.universal.sdk.plugin;

import org.junit.jupiter.api.Test;
import org.openapitools.codegen.ClientOptInput;
import org.openapitools.codegen.DefaultGenerator;
import org.openapitools.codegen.config.CodegenConfigurator;

public class SdkGeneratorTest {

    private static final String SDK_NAME = "python-sdk";
    private static final String SPEC_NAME = "../../spec/rest/api/openapi-account-fee.json";
    private static final String SPEC_ENTRY_NAME = "../../spec/rest/entry/openapi-account.json";
    private static final String WS_SPEC_NAME = "../../spec/ws/openapi-futures-private.json";

    @Test
    public void launchCodeGenerator() {
        {
            final CodegenConfigurator configurator = new CodegenConfigurator()
                    .setGeneratorName(SDK_NAME)
                    .setInputSpec(SPEC_NAME)
                    .setValidateSpec(false)
                    .addAdditionalProperty("GEN_MODE", "API")
                    .setOutputDir("out");

            final ClientOptInput clientOptInput = configurator.toClientOptInput();
            DefaultGenerator generator = new DefaultGenerator();
            generator.opts(clientOptInput).generate();
        }
        {
            final CodegenConfigurator configurator = new CodegenConfigurator()
                    .setGeneratorName(SDK_NAME)
                    .setInputSpec(SPEC_ENTRY_NAME)
                    .setValidateSpec(false)
                    .addAdditionalProperty("GEN_MODE", "ENTRY")
                    .setOutputDir("out");

            final ClientOptInput clientOptInput = configurator.toClientOptInput();
            DefaultGenerator generator = new DefaultGenerator();
            generator.opts(clientOptInput).generate();
        }

        {
            final CodegenConfigurator configurator = new CodegenConfigurator()
                    .setGeneratorName(SDK_NAME)
                    .setInputSpec(SPEC_NAME)
                    .setValidateSpec(false)
                    .addAdditionalProperty("GEN_MODE", "TEST")
                    .setOutputDir("out");

            final ClientOptInput clientOptInput = configurator.toClientOptInput();
            DefaultGenerator generator = new DefaultGenerator();
            generator.opts(clientOptInput).generate();
        }
    }

    @Test
    public void launchCodeGeneratorWs() {
        {
            final CodegenConfigurator configurator = new CodegenConfigurator()
                    .setGeneratorName(SDK_NAME)
                    .setInputSpec(WS_SPEC_NAME)
                    .setValidateSpec(false)
                    .addAdditionalProperty("GEN_MODE", "WS")
                    .setOutputDir("out");

            final ClientOptInput clientOptInput = configurator.toClientOptInput();
            DefaultGenerator generator = new DefaultGenerator();
            generator.opts(clientOptInput).generate();
        }

        {
            final CodegenConfigurator configurator = new CodegenConfigurator()
                    .setGeneratorName(SDK_NAME)
                    .setInputSpec(WS_SPEC_NAME)
                    .setValidateSpec(false)
                    .addAdditionalProperty("GEN_MODE", "WS_TEST")
                    .setOutputDir("out");

            final ClientOptInput clientOptInput = configurator.toClientOptInput();
            DefaultGenerator generator = new DefaultGenerator();
            generator.opts(clientOptInput).generate();
        }
    }

    @Test
    public void launchCodeGeneratorTemplate() {
        {
            final CodegenConfigurator configurator = new CodegenConfigurator()
                    .setGeneratorName(SDK_NAME)
                    .setInputSpec(SPEC_NAME)
                    .setValidateSpec(false)
                    .addAdditionalProperty("GEN_MODE", "test_template")
                    .setOutputDir("out");

            final ClientOptInput clientOptInput = configurator.toClientOptInput();
            DefaultGenerator generator = new DefaultGenerator();
            generator.opts(clientOptInput).generate();
        }
    }
}