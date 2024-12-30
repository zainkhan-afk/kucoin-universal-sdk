// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package subaccount

// ModifySubAccountApiReq struct for ModifySubAccountApiReq
type ModifySubAccountApiReq struct {
	// Password(Must contain 7-32 characters. Cannot contain any spaces.)
	Passphrase string `json:"passphrase,omitempty"`
	// [Permissions](https://www.kucoin.com/docs-new/doc-338144)(Only General、Spot、Futures、Margin、InnerTransfer(Flex Transfer) permissions can be set, such as \"General, Trade\". The default is \"General\")
	Permission *string `json:"permission,omitempty"`
	// IP whitelist(You may add up to 20 IPs. Use a halfwidth comma to each IP)
	IpWhitelist *string `json:"ipWhitelist,omitempty"`
	// API expiration time; Never expire(default)-1，30Day30，90Day90，180Day180，360Day360
	Expire *string `json:"expire,omitempty"`
	// Sub-account name, create sub account name of API Key.
	SubName string `json:"subName,omitempty"`
	// API-Key(Sub-account APIKey)
	ApiKey string `json:"apiKey,omitempty"`
}

// NewModifySubAccountApiReq instantiates a new ModifySubAccountApiReq object
// This constructor will assign default values to properties that have it defined
func NewModifySubAccountApiReq(passphrase string, subName string, apiKey string) *ModifySubAccountApiReq {
	this := ModifySubAccountApiReq{}
	this.Passphrase = passphrase
	var permission string = "General"
	this.Permission = &permission
	var expire string = "-1"
	this.Expire = &expire
	this.SubName = subName
	this.ApiKey = apiKey
	return &this
}

// NewModifySubAccountApiReqWithDefaults instantiates a new ModifySubAccountApiReq object
// This constructor will only assign default values to properties that have it defined,
func NewModifySubAccountApiReqWithDefaults() *ModifySubAccountApiReq {
	this := ModifySubAccountApiReq{}
	var permission string = "General"
	this.Permission = &permission
	var expire string = "-1"
	this.Expire = &expire
	return &this
}

func (o *ModifySubAccountApiReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["passphrase"] = o.Passphrase
	toSerialize["permission"] = o.Permission
	toSerialize["ipWhitelist"] = o.IpWhitelist
	toSerialize["expire"] = o.Expire
	toSerialize["subName"] = o.SubName
	toSerialize["apiKey"] = o.ApiKey
	return toSerialize
}

type ModifySubAccountApiReqBuilder struct {
	obj *ModifySubAccountApiReq
}

func NewModifySubAccountApiReqBuilder() *ModifySubAccountApiReqBuilder {
	return &ModifySubAccountApiReqBuilder{obj: NewModifySubAccountApiReqWithDefaults()}
}

// Password(Must contain 7-32 characters. Cannot contain any spaces.)
func (builder *ModifySubAccountApiReqBuilder) SetPassphrase(value string) *ModifySubAccountApiReqBuilder {
	builder.obj.Passphrase = value
	return builder
}

// [Permissions](https://www.kucoin.com/docs-new/doc-338144)(Only General、Spot、Futures、Margin、InnerTransfer(Flex Transfer) permissions can be set, such as \"General, Trade\". The default is \"General\")
func (builder *ModifySubAccountApiReqBuilder) SetPermission(value string) *ModifySubAccountApiReqBuilder {
	builder.obj.Permission = &value
	return builder
}

// IP whitelist(You may add up to 20 IPs. Use a halfwidth comma to each IP)
func (builder *ModifySubAccountApiReqBuilder) SetIpWhitelist(value string) *ModifySubAccountApiReqBuilder {
	builder.obj.IpWhitelist = &value
	return builder
}

// API expiration time; Never expire(default)-1，30Day30，90Day90，180Day180，360Day360
func (builder *ModifySubAccountApiReqBuilder) SetExpire(value string) *ModifySubAccountApiReqBuilder {
	builder.obj.Expire = &value
	return builder
}

// Sub-account name, create sub account name of API Key.
func (builder *ModifySubAccountApiReqBuilder) SetSubName(value string) *ModifySubAccountApiReqBuilder {
	builder.obj.SubName = value
	return builder
}

// API-Key(Sub-account APIKey)
func (builder *ModifySubAccountApiReqBuilder) SetApiKey(value string) *ModifySubAccountApiReqBuilder {
	builder.obj.ApiKey = value
	return builder
}

func (builder *ModifySubAccountApiReqBuilder) Build() *ModifySubAccountApiReq {
	return builder.obj
}
