class CThostFtdcDisseminationField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.SequenceSeries = data_dict['SequenceSeries']
            self.SequenceNo = data_dict['SequenceNo']
        else:
            self.SequenceSeries = 0
            self.SequenceNo = 0

class CThostFtdcReqUserLoginField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.Password = data_dict['Password']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.InterfaceProductInfo = data_dict['InterfaceProductInfo']
            self.ProtocolInfo = data_dict['ProtocolInfo']
            self.MacAddress = data_dict['MacAddress']
            self.OneTimePassword = data_dict['OneTimePassword']
            self.reserve1 = data_dict['reserve1']
            self.LoginRemark = data_dict['LoginRemark']
            self.ClientIPPort = data_dict['ClientIPPort']
            self.ClientIPAddress = data_dict['ClientIPAddress']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''
            self.Password = ''
            self.UserProductInfo = ''
            self.InterfaceProductInfo = ''
            self.ProtocolInfo = ''
            self.MacAddress = ''
            self.OneTimePassword = ''
            self.reserve1 = ''
            self.LoginRemark = ''
            self.ClientIPPort = 0
            self.ClientIPAddress = ''

class CThostFtdcRspUserLoginField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.LoginTime = data_dict['LoginTime']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.SystemName = data_dict['SystemName']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.MaxOrderRef = data_dict['MaxOrderRef']
            self.SHFETime = data_dict['SHFETime']
            self.DCETime = data_dict['DCETime']
            self.CZCETime = data_dict['CZCETime']
            self.FFEXTime = data_dict['FFEXTime']
            self.INETime = data_dict['INETime']
        else:
            self.TradingDay = ''
            self.LoginTime = ''
            self.BrokerID = ''
            self.UserID = ''
            self.SystemName = ''
            self.FrontID = 0
            self.SessionID = 0
            self.MaxOrderRef = ''
            self.SHFETime = ''
            self.DCETime = ''
            self.CZCETime = ''
            self.FFEXTime = ''
            self.INETime = ''

class CThostFtdcUserLogoutField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcForceUserLogoutField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcReqAuthenticateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.AuthCode = data_dict['AuthCode']
            self.AppID = data_dict['AppID']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserProductInfo = ''
            self.AuthCode = ''
            self.AppID = ''

class CThostFtdcRspAuthenticateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.AppID = data_dict['AppID']
            self.AppType = chr(data_dict['AppType'])
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserProductInfo = ''
            self.AppID = ''
            self.AppType = ''

class CThostFtdcAuthenticationInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.AuthInfo = data_dict['AuthInfo']
            self.IsResult = data_dict['IsResult']
            self.AppID = data_dict['AppID']
            self.AppType = chr(data_dict['AppType'])
            self.reserve1 = data_dict['reserve1']
            self.ClientIPAddress = data_dict['ClientIPAddress']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserProductInfo = ''
            self.AuthInfo = ''
            self.IsResult = 0
            self.AppID = ''
            self.AppType = ''
            self.reserve1 = ''
            self.ClientIPAddress = ''

class CThostFtdcRspUserLogin2Field:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.LoginTime = data_dict['LoginTime']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.SystemName = data_dict['SystemName']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.MaxOrderRef = data_dict['MaxOrderRef']
            self.SHFETime = data_dict['SHFETime']
            self.DCETime = data_dict['DCETime']
            self.CZCETime = data_dict['CZCETime']
            self.FFEXTime = data_dict['FFEXTime']
            self.INETime = data_dict['INETime']
            self.RandomString = data_dict['RandomString']
        else:
            self.TradingDay = ''
            self.LoginTime = ''
            self.BrokerID = ''
            self.UserID = ''
            self.SystemName = ''
            self.FrontID = 0
            self.SessionID = 0
            self.MaxOrderRef = ''
            self.SHFETime = ''
            self.DCETime = ''
            self.CZCETime = ''
            self.FFEXTime = ''
            self.INETime = ''
            self.RandomString = ''

class CThostFtdcTransferHeaderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.Version = data_dict['Version']
            self.TradeCode = data_dict['TradeCode']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.TradeSerial = data_dict['TradeSerial']
            self.FutureID = data_dict['FutureID']
            self.BankID = data_dict['BankID']
            self.BankBrchID = data_dict['BankBrchID']
            self.OperNo = data_dict['OperNo']
            self.DeviceID = data_dict['DeviceID']
            self.RecordNum = data_dict['RecordNum']
            self.SessionID = data_dict['SessionID']
            self.RequestID = data_dict['RequestID']
        else:
            self.Version = ''
            self.TradeCode = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.TradeSerial = ''
            self.FutureID = ''
            self.BankID = ''
            self.BankBrchID = ''
            self.OperNo = ''
            self.DeviceID = ''
            self.RecordNum = ''
            self.SessionID = 0
            self.RequestID = 0

class CThostFtdcTransferBankToFutureReqField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FutureAccount = data_dict['FutureAccount']
            self.FuturePwdFlag = chr(data_dict['FuturePwdFlag'])
            self.FutureAccPwd = data_dict['FutureAccPwd']
            self.TradeAmt = data_dict['TradeAmt']
            self.CustFee = data_dict['CustFee']
            self.CurrencyCode = data_dict['CurrencyCode']
        else:
            self.FutureAccount = ''
            self.FuturePwdFlag = ''
            self.FutureAccPwd = ''
            self.TradeAmt = 0.0
            self.CustFee = 0.0
            self.CurrencyCode = ''

class CThostFtdcTransferBankToFutureRspField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.RetCode = data_dict['RetCode']
            self.RetInfo = data_dict['RetInfo']
            self.FutureAccount = data_dict['FutureAccount']
            self.TradeAmt = data_dict['TradeAmt']
            self.CustFee = data_dict['CustFee']
            self.CurrencyCode = data_dict['CurrencyCode']
        else:
            self.RetCode = ''
            self.RetInfo = ''
            self.FutureAccount = ''
            self.TradeAmt = 0.0
            self.CustFee = 0.0
            self.CurrencyCode = ''

class CThostFtdcTransferFutureToBankReqField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FutureAccount = data_dict['FutureAccount']
            self.FuturePwdFlag = chr(data_dict['FuturePwdFlag'])
            self.FutureAccPwd = data_dict['FutureAccPwd']
            self.TradeAmt = data_dict['TradeAmt']
            self.CustFee = data_dict['CustFee']
            self.CurrencyCode = data_dict['CurrencyCode']
        else:
            self.FutureAccount = ''
            self.FuturePwdFlag = ''
            self.FutureAccPwd = ''
            self.TradeAmt = 0.0
            self.CustFee = 0.0
            self.CurrencyCode = ''

class CThostFtdcTransferFutureToBankRspField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.RetCode = data_dict['RetCode']
            self.RetInfo = data_dict['RetInfo']
            self.FutureAccount = data_dict['FutureAccount']
            self.TradeAmt = data_dict['TradeAmt']
            self.CustFee = data_dict['CustFee']
            self.CurrencyCode = data_dict['CurrencyCode']
        else:
            self.RetCode = ''
            self.RetInfo = ''
            self.FutureAccount = ''
            self.TradeAmt = 0.0
            self.CustFee = 0.0
            self.CurrencyCode = ''

class CThostFtdcTransferQryBankReqField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FutureAccount = data_dict['FutureAccount']
            self.FuturePwdFlag = chr(data_dict['FuturePwdFlag'])
            self.FutureAccPwd = data_dict['FutureAccPwd']
            self.CurrencyCode = data_dict['CurrencyCode']
        else:
            self.FutureAccount = ''
            self.FuturePwdFlag = ''
            self.FutureAccPwd = ''
            self.CurrencyCode = ''

class CThostFtdcTransferQryBankRspField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.RetCode = data_dict['RetCode']
            self.RetInfo = data_dict['RetInfo']
            self.FutureAccount = data_dict['FutureAccount']
            self.TradeAmt = data_dict['TradeAmt']
            self.UseAmt = data_dict['UseAmt']
            self.FetchAmt = data_dict['FetchAmt']
            self.CurrencyCode = data_dict['CurrencyCode']
        else:
            self.RetCode = ''
            self.RetInfo = ''
            self.FutureAccount = ''
            self.TradeAmt = 0.0
            self.UseAmt = 0.0
            self.FetchAmt = 0.0
            self.CurrencyCode = ''

class CThostFtdcTransferQryDetailReqField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FutureAccount = data_dict['FutureAccount']
        else:
            self.FutureAccount = ''

class CThostFtdcTransferQryDetailRspField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.TradeCode = data_dict['TradeCode']
            self.FutureSerial = data_dict['FutureSerial']
            self.FutureID = data_dict['FutureID']
            self.FutureAccount = data_dict['FutureAccount']
            self.BankSerial = data_dict['BankSerial']
            self.BankID = data_dict['BankID']
            self.BankBrchID = data_dict['BankBrchID']
            self.BankAccount = data_dict['BankAccount']
            self.CertCode = data_dict['CertCode']
            self.CurrencyCode = data_dict['CurrencyCode']
            self.TxAmount = data_dict['TxAmount']
            self.Flag = chr(data_dict['Flag'])
        else:
            self.TradeDate = ''
            self.TradeTime = ''
            self.TradeCode = ''
            self.FutureSerial = 0
            self.FutureID = ''
            self.FutureAccount = ''
            self.BankSerial = 0
            self.BankID = ''
            self.BankBrchID = ''
            self.BankAccount = ''
            self.CertCode = ''
            self.CurrencyCode = ''
            self.TxAmount = 0.0
            self.Flag = ''

class CThostFtdcRspInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcExchangeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ExchangeName = data_dict['ExchangeName']
            self.ExchangeProperty = chr(data_dict['ExchangeProperty'])
        else:
            self.ExchangeID = ''
            self.ExchangeName = ''
            self.ExchangeProperty = ''

class CThostFtdcProductField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ProductName = data_dict['ProductName']
            self.ExchangeID = data_dict['ExchangeID']
            self.ProductClass = chr(data_dict['ProductClass'])
            self.VolumeMultiple = data_dict['VolumeMultiple']
            self.PriceTick = data_dict['PriceTick']
            self.MaxMarketOrderVolume = data_dict['MaxMarketOrderVolume']
            self.MinMarketOrderVolume = data_dict['MinMarketOrderVolume']
            self.MaxLimitOrderVolume = data_dict['MaxLimitOrderVolume']
            self.MinLimitOrderVolume = data_dict['MinLimitOrderVolume']
            self.PositionType = chr(data_dict['PositionType'])
            self.PositionDateType = chr(data_dict['PositionDateType'])
            self.CloseDealType = chr(data_dict['CloseDealType'])
            self.TradeCurrencyID = data_dict['TradeCurrencyID']
            self.MortgageFundUseRange = chr(data_dict['MortgageFundUseRange'])
            self.reserve2 = data_dict['reserve2']
            self.UnderlyingMultiple = data_dict['UnderlyingMultiple']
            self.ProductID = data_dict['ProductID']
            self.ExchangeProductID = data_dict['ExchangeProductID']
        else:
            self.reserve1 = ''
            self.ProductName = ''
            self.ExchangeID = ''
            self.ProductClass = ''
            self.VolumeMultiple = 0
            self.PriceTick = 0.0
            self.MaxMarketOrderVolume = 0
            self.MinMarketOrderVolume = 0
            self.MaxLimitOrderVolume = 0
            self.MinLimitOrderVolume = 0
            self.PositionType = ''
            self.PositionDateType = ''
            self.CloseDealType = ''
            self.TradeCurrencyID = ''
            self.MortgageFundUseRange = ''
            self.reserve2 = ''
            self.UnderlyingMultiple = 0.0
            self.ProductID = ''
            self.ExchangeProductID = ''

class CThostFtdcInstrumentField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentName = data_dict['InstrumentName']
            self.reserve2 = data_dict['reserve2']
            self.reserve3 = data_dict['reserve3']
            self.ProductClass = chr(data_dict['ProductClass'])
            self.DeliveryYear = data_dict['DeliveryYear']
            self.DeliveryMonth = data_dict['DeliveryMonth']
            self.MaxMarketOrderVolume = data_dict['MaxMarketOrderVolume']
            self.MinMarketOrderVolume = data_dict['MinMarketOrderVolume']
            self.MaxLimitOrderVolume = data_dict['MaxLimitOrderVolume']
            self.MinLimitOrderVolume = data_dict['MinLimitOrderVolume']
            self.VolumeMultiple = data_dict['VolumeMultiple']
            self.PriceTick = data_dict['PriceTick']
            self.CreateDate = data_dict['CreateDate']
            self.OpenDate = data_dict['OpenDate']
            self.ExpireDate = data_dict['ExpireDate']
            self.StartDelivDate = data_dict['StartDelivDate']
            self.EndDelivDate = data_dict['EndDelivDate']
            self.InstLifePhase = chr(data_dict['InstLifePhase'])
            self.IsTrading = data_dict['IsTrading']
            self.PositionType = chr(data_dict['PositionType'])
            self.PositionDateType = chr(data_dict['PositionDateType'])
            self.LongMarginRatio = data_dict['LongMarginRatio']
            self.ShortMarginRatio = data_dict['ShortMarginRatio']
            self.MaxMarginSideAlgorithm = chr(data_dict['MaxMarginSideAlgorithm'])
            self.reserve4 = data_dict['reserve4']
            self.StrikePrice = data_dict['StrikePrice']
            self.OptionsType = chr(data_dict['OptionsType'])
            self.UnderlyingMultiple = data_dict['UnderlyingMultiple']
            self.CombinationType = chr(data_dict['CombinationType'])
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.ProductID = data_dict['ProductID']
            self.UnderlyingInstrID = data_dict['UnderlyingInstrID']
        else:
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InstrumentName = ''
            self.reserve2 = ''
            self.reserve3 = ''
            self.ProductClass = ''
            self.DeliveryYear = 0
            self.DeliveryMonth = 0
            self.MaxMarketOrderVolume = 0
            self.MinMarketOrderVolume = 0
            self.MaxLimitOrderVolume = 0
            self.MinLimitOrderVolume = 0
            self.VolumeMultiple = 0
            self.PriceTick = 0.0
            self.CreateDate = ''
            self.OpenDate = ''
            self.ExpireDate = ''
            self.StartDelivDate = ''
            self.EndDelivDate = ''
            self.InstLifePhase = ''
            self.IsTrading = 0
            self.PositionType = ''
            self.PositionDateType = ''
            self.LongMarginRatio = 0.0
            self.ShortMarginRatio = 0.0
            self.MaxMarginSideAlgorithm = ''
            self.reserve4 = ''
            self.StrikePrice = 0.0
            self.OptionsType = ''
            self.UnderlyingMultiple = 0.0
            self.CombinationType = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.ProductID = ''
            self.UnderlyingInstrID = ''

class CThostFtdcBrokerField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.BrokerAbbr = data_dict['BrokerAbbr']
            self.BrokerName = data_dict['BrokerName']
            self.IsActive = data_dict['IsActive']
        else:
            self.BrokerID = ''
            self.BrokerAbbr = ''
            self.BrokerName = ''
            self.IsActive = 0

class CThostFtdcTraderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ParticipantID = data_dict['ParticipantID']
            self.Password = data_dict['Password']
            self.InstallCount = data_dict['InstallCount']
            self.BrokerID = data_dict['BrokerID']
        else:
            self.ExchangeID = ''
            self.TraderID = ''
            self.ParticipantID = ''
            self.Password = ''
            self.InstallCount = 0
            self.BrokerID = ''

class CThostFtdcInvestorField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InvestorID = data_dict['InvestorID']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorGroupID = data_dict['InvestorGroupID']
            self.InvestorName = data_dict['InvestorName']
            self.IdentifiedCardType = chr(data_dict['IdentifiedCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.IsActive = data_dict['IsActive']
            self.Telephone = data_dict['Telephone']
            self.Address = data_dict['Address']
            self.OpenDate = data_dict['OpenDate']
            self.Mobile = data_dict['Mobile']
            self.CommModelID = data_dict['CommModelID']
            self.MarginModelID = data_dict['MarginModelID']
        else:
            self.InvestorID = ''
            self.BrokerID = ''
            self.InvestorGroupID = ''
            self.InvestorName = ''
            self.IdentifiedCardType = ''
            self.IdentifiedCardNo = ''
            self.IsActive = 0
            self.Telephone = ''
            self.Address = ''
            self.OpenDate = ''
            self.Mobile = ''
            self.CommModelID = ''
            self.MarginModelID = ''

class CThostFtdcTradingCodeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InvestorID = data_dict['InvestorID']
            self.BrokerID = data_dict['BrokerID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ClientID = data_dict['ClientID']
            self.IsActive = data_dict['IsActive']
            self.ClientIDType = chr(data_dict['ClientIDType'])
            self.BranchID = data_dict['BranchID']
            self.BizType = chr(data_dict['BizType'])
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.InvestorID = ''
            self.BrokerID = ''
            self.ExchangeID = ''
            self.ClientID = ''
            self.IsActive = 0
            self.ClientIDType = ''
            self.BranchID = ''
            self.BizType = ''
            self.InvestUnitID = ''

class CThostFtdcPartBrokerField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.IsActive = data_dict['IsActive']
        else:
            self.BrokerID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.IsActive = 0

class CThostFtdcSuperUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.UserID = data_dict['UserID']
            self.UserName = data_dict['UserName']
            self.Password = data_dict['Password']
            self.IsActive = data_dict['IsActive']
        else:
            self.UserID = ''
            self.UserName = ''
            self.Password = ''
            self.IsActive = 0

class CThostFtdcSuperUserFunctionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.UserID = data_dict['UserID']
            self.FunctionCode = chr(data_dict['FunctionCode'])
        else:
            self.UserID = ''
            self.FunctionCode = ''

class CThostFtdcInvestorGroupField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorGroupID = data_dict['InvestorGroupID']
            self.InvestorGroupName = data_dict['InvestorGroupName']
        else:
            self.BrokerID = ''
            self.InvestorGroupID = ''
            self.InvestorGroupName = ''

class CThostFtdcTradingAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.PreMortgage = data_dict['PreMortgage']
            self.PreCredit = data_dict['PreCredit']
            self.PreDeposit = data_dict['PreDeposit']
            self.PreBalance = data_dict['PreBalance']
            self.PreMargin = data_dict['PreMargin']
            self.InterestBase = data_dict['InterestBase']
            self.Interest = data_dict['Interest']
            self.Deposit = data_dict['Deposit']
            self.Withdraw = data_dict['Withdraw']
            self.FrozenMargin = data_dict['FrozenMargin']
            self.FrozenCash = data_dict['FrozenCash']
            self.FrozenCommission = data_dict['FrozenCommission']
            self.CurrMargin = data_dict['CurrMargin']
            self.CashIn = data_dict['CashIn']
            self.Commission = data_dict['Commission']
            self.CloseProfit = data_dict['CloseProfit']
            self.PositionProfit = data_dict['PositionProfit']
            self.Balance = data_dict['Balance']
            self.Available = data_dict['Available']
            self.WithdrawQuota = data_dict['WithdrawQuota']
            self.Reserve = data_dict['Reserve']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.Credit = data_dict['Credit']
            self.Mortgage = data_dict['Mortgage']
            self.ExchangeMargin = data_dict['ExchangeMargin']
            self.DeliveryMargin = data_dict['DeliveryMargin']
            self.ExchangeDeliveryMargin = data_dict['ExchangeDeliveryMargin']
            self.ReserveBalance = data_dict['ReserveBalance']
            self.CurrencyID = data_dict['CurrencyID']
            self.PreFundMortgageIn = data_dict['PreFundMortgageIn']
            self.PreFundMortgageOut = data_dict['PreFundMortgageOut']
            self.FundMortgageIn = data_dict['FundMortgageIn']
            self.FundMortgageOut = data_dict['FundMortgageOut']
            self.FundMortgageAvailable = data_dict['FundMortgageAvailable']
            self.MortgageableFund = data_dict['MortgageableFund']
            self.SpecProductMargin = data_dict['SpecProductMargin']
            self.SpecProductFrozenMargin = data_dict['SpecProductFrozenMargin']
            self.SpecProductCommission = data_dict['SpecProductCommission']
            self.SpecProductFrozenCommission = data_dict['SpecProductFrozenCommission']
            self.SpecProductPositionProfit = data_dict['SpecProductPositionProfit']
            self.SpecProductCloseProfit = data_dict['SpecProductCloseProfit']
            self.SpecProductPositionProfitByAlg = data_dict['SpecProductPositionProfitByAlg']
            self.SpecProductExchangeMargin = data_dict['SpecProductExchangeMargin']
            self.BizType = chr(data_dict['BizType'])
            self.FrozenSwap = data_dict['FrozenSwap']
            self.RemainSwap = data_dict['RemainSwap']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.PreMortgage = 0.0
            self.PreCredit = 0.0
            self.PreDeposit = 0.0
            self.PreBalance = 0.0
            self.PreMargin = 0.0
            self.InterestBase = 0.0
            self.Interest = 0.0
            self.Deposit = 0.0
            self.Withdraw = 0.0
            self.FrozenMargin = 0.0
            self.FrozenCash = 0.0
            self.FrozenCommission = 0.0
            self.CurrMargin = 0.0
            self.CashIn = 0.0
            self.Commission = 0.0
            self.CloseProfit = 0.0
            self.PositionProfit = 0.0
            self.Balance = 0.0
            self.Available = 0.0
            self.WithdrawQuota = 0.0
            self.Reserve = 0.0
            self.TradingDay = ''
            self.SettlementID = 0
            self.Credit = 0.0
            self.Mortgage = 0.0
            self.ExchangeMargin = 0.0
            self.DeliveryMargin = 0.0
            self.ExchangeDeliveryMargin = 0.0
            self.ReserveBalance = 0.0
            self.CurrencyID = ''
            self.PreFundMortgageIn = 0.0
            self.PreFundMortgageOut = 0.0
            self.FundMortgageIn = 0.0
            self.FundMortgageOut = 0.0
            self.FundMortgageAvailable = 0.0
            self.MortgageableFund = 0.0
            self.SpecProductMargin = 0.0
            self.SpecProductFrozenMargin = 0.0
            self.SpecProductCommission = 0.0
            self.SpecProductFrozenCommission = 0.0
            self.SpecProductPositionProfit = 0.0
            self.SpecProductCloseProfit = 0.0
            self.SpecProductPositionProfitByAlg = 0.0
            self.SpecProductExchangeMargin = 0.0
            self.BizType = ''
            self.FrozenSwap = 0.0
            self.RemainSwap = 0.0

class CThostFtdcInvestorPositionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.PosiDirection = chr(data_dict['PosiDirection'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.PositionDate = chr(data_dict['PositionDate'])
            self.YdPosition = data_dict['YdPosition']
            self.Position = data_dict['Position']
            self.LongFrozen = data_dict['LongFrozen']
            self.ShortFrozen = data_dict['ShortFrozen']
            self.LongFrozenAmount = data_dict['LongFrozenAmount']
            self.ShortFrozenAmount = data_dict['ShortFrozenAmount']
            self.OpenVolume = data_dict['OpenVolume']
            self.CloseVolume = data_dict['CloseVolume']
            self.OpenAmount = data_dict['OpenAmount']
            self.CloseAmount = data_dict['CloseAmount']
            self.PositionCost = data_dict['PositionCost']
            self.PreMargin = data_dict['PreMargin']
            self.UseMargin = data_dict['UseMargin']
            self.FrozenMargin = data_dict['FrozenMargin']
            self.FrozenCash = data_dict['FrozenCash']
            self.FrozenCommission = data_dict['FrozenCommission']
            self.CashIn = data_dict['CashIn']
            self.Commission = data_dict['Commission']
            self.CloseProfit = data_dict['CloseProfit']
            self.PositionProfit = data_dict['PositionProfit']
            self.PreSettlementPrice = data_dict['PreSettlementPrice']
            self.SettlementPrice = data_dict['SettlementPrice']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OpenCost = data_dict['OpenCost']
            self.ExchangeMargin = data_dict['ExchangeMargin']
            self.CombPosition = data_dict['CombPosition']
            self.CombLongFrozen = data_dict['CombLongFrozen']
            self.CombShortFrozen = data_dict['CombShortFrozen']
            self.CloseProfitByDate = data_dict['CloseProfitByDate']
            self.CloseProfitByTrade = data_dict['CloseProfitByTrade']
            self.TodayPosition = data_dict['TodayPosition']
            self.MarginRateByMoney = data_dict['MarginRateByMoney']
            self.MarginRateByVolume = data_dict['MarginRateByVolume']
            self.StrikeFrozen = data_dict['StrikeFrozen']
            self.StrikeFrozenAmount = data_dict['StrikeFrozenAmount']
            self.AbandonFrozen = data_dict['AbandonFrozen']
            self.ExchangeID = data_dict['ExchangeID']
            self.YdStrikeFrozen = data_dict['YdStrikeFrozen']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.PositionCostOffset = data_dict['PositionCostOffset']
            self.TasPosition = data_dict['TasPosition']
            self.TasPositionCost = data_dict['TasPositionCost']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.PosiDirection = ''
            self.HedgeFlag = ''
            self.PositionDate = ''
            self.YdPosition = 0
            self.Position = 0
            self.LongFrozen = 0
            self.ShortFrozen = 0
            self.LongFrozenAmount = 0.0
            self.ShortFrozenAmount = 0.0
            self.OpenVolume = 0
            self.CloseVolume = 0
            self.OpenAmount = 0.0
            self.CloseAmount = 0.0
            self.PositionCost = 0.0
            self.PreMargin = 0.0
            self.UseMargin = 0.0
            self.FrozenMargin = 0.0
            self.FrozenCash = 0.0
            self.FrozenCommission = 0.0
            self.CashIn = 0.0
            self.Commission = 0.0
            self.CloseProfit = 0.0
            self.PositionProfit = 0.0
            self.PreSettlementPrice = 0.0
            self.SettlementPrice = 0.0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OpenCost = 0.0
            self.ExchangeMargin = 0.0
            self.CombPosition = 0
            self.CombLongFrozen = 0
            self.CombShortFrozen = 0
            self.CloseProfitByDate = 0.0
            self.CloseProfitByTrade = 0.0
            self.TodayPosition = 0
            self.MarginRateByMoney = 0.0
            self.MarginRateByVolume = 0.0
            self.StrikeFrozen = 0
            self.StrikeFrozenAmount = 0.0
            self.AbandonFrozen = 0
            self.ExchangeID = ''
            self.YdStrikeFrozen = 0
            self.InvestUnitID = ''
            self.PositionCostOffset = 0.0
            self.TasPosition = 0
            self.TasPositionCost = 0.0
            self.InstrumentID = ''

class CThostFtdcInstrumentMarginRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.LongMarginRatioByMoney = data_dict['LongMarginRatioByMoney']
            self.LongMarginRatioByVolume = data_dict['LongMarginRatioByVolume']
            self.ShortMarginRatioByMoney = data_dict['ShortMarginRatioByMoney']
            self.ShortMarginRatioByVolume = data_dict['ShortMarginRatioByVolume']
            self.IsRelative = data_dict['IsRelative']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.HedgeFlag = ''
            self.LongMarginRatioByMoney = 0.0
            self.LongMarginRatioByVolume = 0.0
            self.ShortMarginRatioByMoney = 0.0
            self.ShortMarginRatioByVolume = 0.0
            self.IsRelative = 0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcInstrumentCommissionRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OpenRatioByMoney = data_dict['OpenRatioByMoney']
            self.OpenRatioByVolume = data_dict['OpenRatioByVolume']
            self.CloseRatioByMoney = data_dict['CloseRatioByMoney']
            self.CloseRatioByVolume = data_dict['CloseRatioByVolume']
            self.CloseTodayRatioByMoney = data_dict['CloseTodayRatioByMoney']
            self.CloseTodayRatioByVolume = data_dict['CloseTodayRatioByVolume']
            self.ExchangeID = data_dict['ExchangeID']
            self.BizType = chr(data_dict['BizType'])
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.OpenRatioByMoney = 0.0
            self.OpenRatioByVolume = 0.0
            self.CloseRatioByMoney = 0.0
            self.CloseRatioByVolume = 0.0
            self.CloseTodayRatioByMoney = 0.0
            self.CloseTodayRatioByVolume = 0.0
            self.ExchangeID = ''
            self.BizType = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcDepthMarketDataField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve2 = data_dict['reserve2']
            self.LastPrice = data_dict['LastPrice']
            self.PreSettlementPrice = data_dict['PreSettlementPrice']
            self.PreClosePrice = data_dict['PreClosePrice']
            self.PreOpenInterest = data_dict['PreOpenInterest']
            self.OpenPrice = data_dict['OpenPrice']
            self.HighestPrice = data_dict['HighestPrice']
            self.LowestPrice = data_dict['LowestPrice']
            self.Volume = data_dict['Volume']
            self.Turnover = data_dict['Turnover']
            self.OpenInterest = data_dict['OpenInterest']
            self.ClosePrice = data_dict['ClosePrice']
            self.SettlementPrice = data_dict['SettlementPrice']
            self.UpperLimitPrice = data_dict['UpperLimitPrice']
            self.LowerLimitPrice = data_dict['LowerLimitPrice']
            self.PreDelta = data_dict['PreDelta']
            self.CurrDelta = data_dict['CurrDelta']
            self.UpdateTime = data_dict['UpdateTime']
            self.UpdateMillisec = data_dict['UpdateMillisec']
            self.BidPrice1 = data_dict['BidPrice1']
            self.BidVolume1 = data_dict['BidVolume1']
            self.AskPrice1 = data_dict['AskPrice1']
            self.AskVolume1 = data_dict['AskVolume1']
            self.BidPrice2 = data_dict['BidPrice2']
            self.BidVolume2 = data_dict['BidVolume2']
            self.AskPrice2 = data_dict['AskPrice2']
            self.AskVolume2 = data_dict['AskVolume2']
            self.BidPrice3 = data_dict['BidPrice3']
            self.BidVolume3 = data_dict['BidVolume3']
            self.AskPrice3 = data_dict['AskPrice3']
            self.AskVolume3 = data_dict['AskVolume3']
            self.BidPrice4 = data_dict['BidPrice4']
            self.BidVolume4 = data_dict['BidVolume4']
            self.AskPrice4 = data_dict['AskPrice4']
            self.AskVolume4 = data_dict['AskVolume4']
            self.BidPrice5 = data_dict['BidPrice5']
            self.BidVolume5 = data_dict['BidVolume5']
            self.AskPrice5 = data_dict['AskPrice5']
            self.AskVolume5 = data_dict['AskVolume5']
            self.AveragePrice = data_dict['AveragePrice']
            self.ActionDay = data_dict['ActionDay']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.TradingDay = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.reserve2 = ''
            self.LastPrice = 0.0
            self.PreSettlementPrice = 0.0
            self.PreClosePrice = 0.0
            self.PreOpenInterest = 0.0
            self.OpenPrice = 0.0
            self.HighestPrice = 0.0
            self.LowestPrice = 0.0
            self.Volume = 0
            self.Turnover = 0.0
            self.OpenInterest = 0.0
            self.ClosePrice = 0.0
            self.SettlementPrice = 0.0
            self.UpperLimitPrice = 0.0
            self.LowerLimitPrice = 0.0
            self.PreDelta = 0.0
            self.CurrDelta = 0.0
            self.UpdateTime = ''
            self.UpdateMillisec = 0
            self.BidPrice1 = 0.0
            self.BidVolume1 = 0
            self.AskPrice1 = 0.0
            self.AskVolume1 = 0
            self.BidPrice2 = 0.0
            self.BidVolume2 = 0
            self.AskPrice2 = 0.0
            self.AskVolume2 = 0
            self.BidPrice3 = 0.0
            self.BidVolume3 = 0
            self.AskPrice3 = 0.0
            self.AskVolume3 = 0
            self.BidPrice4 = 0.0
            self.BidVolume4 = 0
            self.AskPrice4 = 0.0
            self.AskVolume4 = 0
            self.BidPrice5 = 0.0
            self.BidVolume5 = 0
            self.AskPrice5 = 0.0
            self.AskVolume5 = 0
            self.AveragePrice = 0.0
            self.ActionDay = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''

class CThostFtdcInstrumentTradingRightField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.TradingRight = chr(data_dict['TradingRight'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.TradingRight = ''
            self.InstrumentID = ''

class CThostFtdcBrokerUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserName = data_dict['UserName']
            self.UserType = chr(data_dict['UserType'])
            self.IsActive = data_dict['IsActive']
            self.IsUsingOTP = data_dict['IsUsingOTP']
            self.IsAuthForce = data_dict['IsAuthForce']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserName = ''
            self.UserType = ''
            self.IsActive = 0
            self.IsUsingOTP = 0
            self.IsAuthForce = 0

class CThostFtdcBrokerUserPasswordField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.Password = data_dict['Password']
            self.LastUpdateTime = data_dict['LastUpdateTime']
            self.LastLoginTime = data_dict['LastLoginTime']
            self.ExpireDate = data_dict['ExpireDate']
            self.WeakExpireDate = data_dict['WeakExpireDate']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.Password = ''
            self.LastUpdateTime = ''
            self.LastLoginTime = ''
            self.ExpireDate = ''
            self.WeakExpireDate = ''

class CThostFtdcBrokerUserFunctionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.BrokerFunctionCode = chr(data_dict['BrokerFunctionCode'])
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.BrokerFunctionCode = ''

class CThostFtdcTraderOfferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ParticipantID = data_dict['ParticipantID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.TraderConnectStatus = chr(data_dict['TraderConnectStatus'])
            self.ConnectRequestDate = data_dict['ConnectRequestDate']
            self.ConnectRequestTime = data_dict['ConnectRequestTime']
            self.LastReportDate = data_dict['LastReportDate']
            self.LastReportTime = data_dict['LastReportTime']
            self.ConnectDate = data_dict['ConnectDate']
            self.ConnectTime = data_dict['ConnectTime']
            self.StartDate = data_dict['StartDate']
            self.StartTime = data_dict['StartTime']
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.MaxTradeID = data_dict['MaxTradeID']
            self.MaxOrderMessageReference = data_dict['MaxOrderMessageReference']
        else:
            self.ExchangeID = ''
            self.TraderID = ''
            self.ParticipantID = ''
            self.Password = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.TraderConnectStatus = ''
            self.ConnectRequestDate = ''
            self.ConnectRequestTime = ''
            self.LastReportDate = ''
            self.LastReportTime = ''
            self.ConnectDate = ''
            self.ConnectTime = ''
            self.StartDate = ''
            self.StartTime = ''
            self.TradingDay = ''
            self.BrokerID = ''
            self.MaxTradeID = ''
            self.MaxOrderMessageReference = ''

class CThostFtdcSettlementInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.SequenceNo = data_dict['SequenceNo']
            self.Content = data_dict['Content']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.TradingDay = ''
            self.SettlementID = 0
            self.BrokerID = ''
            self.InvestorID = ''
            self.SequenceNo = 0
            self.Content = ''
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcInstrumentMarginRateAdjustField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.LongMarginRatioByMoney = data_dict['LongMarginRatioByMoney']
            self.LongMarginRatioByVolume = data_dict['LongMarginRatioByVolume']
            self.ShortMarginRatioByMoney = data_dict['ShortMarginRatioByMoney']
            self.ShortMarginRatioByVolume = data_dict['ShortMarginRatioByVolume']
            self.IsRelative = data_dict['IsRelative']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.HedgeFlag = ''
            self.LongMarginRatioByMoney = 0.0
            self.LongMarginRatioByVolume = 0.0
            self.ShortMarginRatioByMoney = 0.0
            self.ShortMarginRatioByVolume = 0.0
            self.IsRelative = 0
            self.InstrumentID = ''

class CThostFtdcExchangeMarginRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.LongMarginRatioByMoney = data_dict['LongMarginRatioByMoney']
            self.LongMarginRatioByVolume = data_dict['LongMarginRatioByVolume']
            self.ShortMarginRatioByMoney = data_dict['ShortMarginRatioByMoney']
            self.ShortMarginRatioByVolume = data_dict['ShortMarginRatioByVolume']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.LongMarginRatioByMoney = 0.0
            self.LongMarginRatioByVolume = 0.0
            self.ShortMarginRatioByMoney = 0.0
            self.ShortMarginRatioByVolume = 0.0
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcExchangeMarginRateAdjustField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.LongMarginRatioByMoney = data_dict['LongMarginRatioByMoney']
            self.LongMarginRatioByVolume = data_dict['LongMarginRatioByVolume']
            self.ShortMarginRatioByMoney = data_dict['ShortMarginRatioByMoney']
            self.ShortMarginRatioByVolume = data_dict['ShortMarginRatioByVolume']
            self.ExchLongMarginRatioByMoney = data_dict['ExchLongMarginRatioByMoney']
            self.ExchLongMarginRatioByVolume = data_dict['ExchLongMarginRatioByVolume']
            self.ExchShortMarginRatioByMoney = data_dict['ExchShortMarginRatioByMoney']
            self.ExchShortMarginRatioByVolume = data_dict['ExchShortMarginRatioByVolume']
            self.NoLongMarginRatioByMoney = data_dict['NoLongMarginRatioByMoney']
            self.NoLongMarginRatioByVolume = data_dict['NoLongMarginRatioByVolume']
            self.NoShortMarginRatioByMoney = data_dict['NoShortMarginRatioByMoney']
            self.NoShortMarginRatioByVolume = data_dict['NoShortMarginRatioByVolume']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.LongMarginRatioByMoney = 0.0
            self.LongMarginRatioByVolume = 0.0
            self.ShortMarginRatioByMoney = 0.0
            self.ShortMarginRatioByVolume = 0.0
            self.ExchLongMarginRatioByMoney = 0.0
            self.ExchLongMarginRatioByVolume = 0.0
            self.ExchShortMarginRatioByMoney = 0.0
            self.ExchShortMarginRatioByVolume = 0.0
            self.NoLongMarginRatioByMoney = 0.0
            self.NoLongMarginRatioByVolume = 0.0
            self.NoShortMarginRatioByMoney = 0.0
            self.NoShortMarginRatioByVolume = 0.0
            self.InstrumentID = ''

class CThostFtdcExchangeRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.FromCurrencyID = data_dict['FromCurrencyID']
            self.FromCurrencyUnit = data_dict['FromCurrencyUnit']
            self.ToCurrencyID = data_dict['ToCurrencyID']
            self.ExchangeRate = data_dict['ExchangeRate']
        else:
            self.BrokerID = ''
            self.FromCurrencyID = ''
            self.FromCurrencyUnit = 0.0
            self.ToCurrencyID = ''
            self.ExchangeRate = 0.0

class CThostFtdcSettlementRefField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
        else:
            self.TradingDay = ''
            self.SettlementID = 0

class CThostFtdcCurrentTimeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.CurrDate = data_dict['CurrDate']
            self.CurrTime = data_dict['CurrTime']
            self.CurrMillisec = data_dict['CurrMillisec']
            self.ActionDay = data_dict['ActionDay']
        else:
            self.CurrDate = ''
            self.CurrTime = ''
            self.CurrMillisec = 0
            self.ActionDay = ''

class CThostFtdcCommPhaseField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.CommPhaseNo = data_dict['CommPhaseNo']
            self.SystemID = data_dict['SystemID']
        else:
            self.TradingDay = ''
            self.CommPhaseNo = 0
            self.SystemID = ''

class CThostFtdcLoginInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.LoginDate = data_dict['LoginDate']
            self.LoginTime = data_dict['LoginTime']
            self.reserve1 = data_dict['reserve1']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.InterfaceProductInfo = data_dict['InterfaceProductInfo']
            self.ProtocolInfo = data_dict['ProtocolInfo']
            self.SystemName = data_dict['SystemName']
            self.PasswordDeprecated = data_dict['PasswordDeprecated']
            self.MaxOrderRef = data_dict['MaxOrderRef']
            self.SHFETime = data_dict['SHFETime']
            self.DCETime = data_dict['DCETime']
            self.CZCETime = data_dict['CZCETime']
            self.FFEXTime = data_dict['FFEXTime']
            self.MacAddress = data_dict['MacAddress']
            self.OneTimePassword = data_dict['OneTimePassword']
            self.INETime = data_dict['INETime']
            self.IsQryControl = data_dict['IsQryControl']
            self.LoginRemark = data_dict['LoginRemark']
            self.Password = data_dict['Password']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.FrontID = 0
            self.SessionID = 0
            self.BrokerID = ''
            self.UserID = ''
            self.LoginDate = ''
            self.LoginTime = ''
            self.reserve1 = ''
            self.UserProductInfo = ''
            self.InterfaceProductInfo = ''
            self.ProtocolInfo = ''
            self.SystemName = ''
            self.PasswordDeprecated = ''
            self.MaxOrderRef = ''
            self.SHFETime = ''
            self.DCETime = ''
            self.CZCETime = ''
            self.FFEXTime = ''
            self.MacAddress = ''
            self.OneTimePassword = ''
            self.INETime = ''
            self.IsQryControl = 0
            self.LoginRemark = ''
            self.Password = ''
            self.IPAddress = ''

class CThostFtdcLogoutAllField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.SystemName = data_dict['SystemName']
        else:
            self.FrontID = 0
            self.SessionID = 0
            self.SystemName = ''

class CThostFtdcFrontStatusField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontID = data_dict['FrontID']
            self.LastReportDate = data_dict['LastReportDate']
            self.LastReportTime = data_dict['LastReportTime']
            self.IsActive = data_dict['IsActive']
        else:
            self.FrontID = 0
            self.LastReportDate = ''
            self.LastReportTime = ''
            self.IsActive = 0

class CThostFtdcUserPasswordUpdateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.OldPassword = data_dict['OldPassword']
            self.NewPassword = data_dict['NewPassword']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.OldPassword = ''
            self.NewPassword = ''

class CThostFtdcInputOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OrderRef = data_dict['OrderRef']
            self.UserID = data_dict['UserID']
            self.OrderPriceType = chr(data_dict['OrderPriceType'])
            self.Direction = chr(data_dict['Direction'])
            self.CombOffsetFlag = data_dict['CombOffsetFlag']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeTotalOriginal = data_dict['VolumeTotalOriginal']
            self.TimeCondition = chr(data_dict['TimeCondition'])
            self.GTDDate = data_dict['GTDDate']
            self.VolumeCondition = chr(data_dict['VolumeCondition'])
            self.MinVolume = data_dict['MinVolume']
            self.ContingentCondition = chr(data_dict['ContingentCondition'])
            self.StopPrice = data_dict['StopPrice']
            self.ForceCloseReason = chr(data_dict['ForceCloseReason'])
            self.IsAutoSuspend = data_dict['IsAutoSuspend']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.RequestID = data_dict['RequestID']
            self.UserForceClose = data_dict['UserForceClose']
            self.IsSwapOrder = data_dict['IsSwapOrder']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OrderRef = ''
            self.UserID = ''
            self.OrderPriceType = ''
            self.Direction = ''
            self.CombOffsetFlag = ''
            self.CombHedgeFlag = ''
            self.LimitPrice = 0.0
            self.VolumeTotalOriginal = 0
            self.TimeCondition = ''
            self.GTDDate = ''
            self.VolumeCondition = ''
            self.MinVolume = 0
            self.ContingentCondition = ''
            self.StopPrice = 0.0
            self.ForceCloseReason = ''
            self.IsAutoSuspend = 0
            self.BusinessUnit = ''
            self.RequestID = 0
            self.UserForceClose = 0
            self.IsSwapOrder = 0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OrderRef = data_dict['OrderRef']
            self.UserID = data_dict['UserID']
            self.OrderPriceType = chr(data_dict['OrderPriceType'])
            self.Direction = chr(data_dict['Direction'])
            self.CombOffsetFlag = data_dict['CombOffsetFlag']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeTotalOriginal = data_dict['VolumeTotalOriginal']
            self.TimeCondition = chr(data_dict['TimeCondition'])
            self.GTDDate = data_dict['GTDDate']
            self.VolumeCondition = chr(data_dict['VolumeCondition'])
            self.MinVolume = data_dict['MinVolume']
            self.ContingentCondition = chr(data_dict['ContingentCondition'])
            self.StopPrice = data_dict['StopPrice']
            self.ForceCloseReason = chr(data_dict['ForceCloseReason'])
            self.IsAutoSuspend = data_dict['IsAutoSuspend']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.RequestID = data_dict['RequestID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OrderSysID = data_dict['OrderSysID']
            self.OrderSource = chr(data_dict['OrderSource'])
            self.OrderStatus = chr(data_dict['OrderStatus'])
            self.OrderType = chr(data_dict['OrderType'])
            self.VolumeTraded = data_dict['VolumeTraded']
            self.VolumeTotal = data_dict['VolumeTotal']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.ActiveTime = data_dict['ActiveTime']
            self.SuspendTime = data_dict['SuspendTime']
            self.UpdateTime = data_dict['UpdateTime']
            self.CancelTime = data_dict['CancelTime']
            self.ActiveTraderID = data_dict['ActiveTraderID']
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.StatusMsg = data_dict['StatusMsg']
            self.UserForceClose = data_dict['UserForceClose']
            self.ActiveUserID = data_dict['ActiveUserID']
            self.BrokerOrderSeq = data_dict['BrokerOrderSeq']
            self.RelativeOrderSysID = data_dict['RelativeOrderSysID']
            self.ZCETotalTradedVolume = data_dict['ZCETotalTradedVolume']
            self.IsSwapOrder = data_dict['IsSwapOrder']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OrderRef = ''
            self.UserID = ''
            self.OrderPriceType = ''
            self.Direction = ''
            self.CombOffsetFlag = ''
            self.CombHedgeFlag = ''
            self.LimitPrice = 0.0
            self.VolumeTotalOriginal = 0
            self.TimeCondition = ''
            self.GTDDate = ''
            self.VolumeCondition = ''
            self.MinVolume = 0
            self.ContingentCondition = ''
            self.StopPrice = 0.0
            self.ForceCloseReason = ''
            self.IsAutoSuspend = 0
            self.BusinessUnit = ''
            self.RequestID = 0
            self.OrderLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OrderSysID = ''
            self.OrderSource = ''
            self.OrderStatus = ''
            self.OrderType = ''
            self.VolumeTraded = 0
            self.VolumeTotal = 0
            self.InsertDate = ''
            self.InsertTime = ''
            self.ActiveTime = ''
            self.SuspendTime = ''
            self.UpdateTime = ''
            self.CancelTime = ''
            self.ActiveTraderID = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.FrontID = 0
            self.SessionID = 0
            self.UserProductInfo = ''
            self.StatusMsg = ''
            self.UserForceClose = 0
            self.ActiveUserID = ''
            self.BrokerOrderSeq = 0
            self.RelativeOrderSysID = ''
            self.ZCETotalTradedVolume = 0
            self.IsSwapOrder = 0
            self.BranchID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcExchangeOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.OrderPriceType = chr(data_dict['OrderPriceType'])
            self.Direction = chr(data_dict['Direction'])
            self.CombOffsetFlag = data_dict['CombOffsetFlag']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeTotalOriginal = data_dict['VolumeTotalOriginal']
            self.TimeCondition = chr(data_dict['TimeCondition'])
            self.GTDDate = data_dict['GTDDate']
            self.VolumeCondition = chr(data_dict['VolumeCondition'])
            self.MinVolume = data_dict['MinVolume']
            self.ContingentCondition = chr(data_dict['ContingentCondition'])
            self.StopPrice = data_dict['StopPrice']
            self.ForceCloseReason = chr(data_dict['ForceCloseReason'])
            self.IsAutoSuspend = data_dict['IsAutoSuspend']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.RequestID = data_dict['RequestID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OrderSysID = data_dict['OrderSysID']
            self.OrderSource = chr(data_dict['OrderSource'])
            self.OrderStatus = chr(data_dict['OrderStatus'])
            self.OrderType = chr(data_dict['OrderType'])
            self.VolumeTraded = data_dict['VolumeTraded']
            self.VolumeTotal = data_dict['VolumeTotal']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.ActiveTime = data_dict['ActiveTime']
            self.SuspendTime = data_dict['SuspendTime']
            self.UpdateTime = data_dict['UpdateTime']
            self.CancelTime = data_dict['CancelTime']
            self.ActiveTraderID = data_dict['ActiveTraderID']
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.BranchID = data_dict['BranchID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.OrderPriceType = ''
            self.Direction = ''
            self.CombOffsetFlag = ''
            self.CombHedgeFlag = ''
            self.LimitPrice = 0.0
            self.VolumeTotalOriginal = 0
            self.TimeCondition = ''
            self.GTDDate = ''
            self.VolumeCondition = ''
            self.MinVolume = 0
            self.ContingentCondition = ''
            self.StopPrice = 0.0
            self.ForceCloseReason = ''
            self.IsAutoSuspend = 0
            self.BusinessUnit = ''
            self.RequestID = 0
            self.OrderLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OrderSysID = ''
            self.OrderSource = ''
            self.OrderStatus = ''
            self.OrderType = ''
            self.VolumeTraded = 0
            self.VolumeTotal = 0
            self.InsertDate = ''
            self.InsertTime = ''
            self.ActiveTime = ''
            self.SuspendTime = ''
            self.UpdateTime = ''
            self.CancelTime = ''
            self.ActiveTraderID = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.BranchID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcExchangeOrderInsertErrorField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcInputOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OrderActionRef = data_dict['OrderActionRef']
            self.OrderRef = data_dict['OrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeChange = data_dict['VolumeChange']
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OrderActionRef = 0
            self.OrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.ActionFlag = ''
            self.LimitPrice = 0.0
            self.VolumeChange = 0
            self.UserID = ''
            self.reserve1 = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OrderActionRef = data_dict['OrderActionRef']
            self.OrderRef = data_dict['OrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeChange = data_dict['VolumeChange']
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.StatusMsg = data_dict['StatusMsg']
            self.reserve1 = data_dict['reserve1']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OrderActionRef = 0
            self.OrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.ActionFlag = ''
            self.LimitPrice = 0.0
            self.VolumeChange = 0
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.StatusMsg = ''
            self.reserve1 = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcExchangeOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeChange = data_dict['VolumeChange']
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.BranchID = data_dict['BranchID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.ActionFlag = ''
            self.LimitPrice = 0.0
            self.VolumeChange = 0
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.BranchID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.IPAddress = ''

class CThostFtdcExchangeOrderActionErrorField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.ActionLocalID = ''
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcExchangeTradeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.TradeID = data_dict['TradeID']
            self.Direction = chr(data_dict['Direction'])
            self.OrderSysID = data_dict['OrderSysID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.TradingRole = chr(data_dict['TradingRole'])
            self.reserve1 = data_dict['reserve1']
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.Price = data_dict['Price']
            self.Volume = data_dict['Volume']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.TradeType = chr(data_dict['TradeType'])
            self.PriceSource = chr(data_dict['PriceSource'])
            self.TraderID = data_dict['TraderID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ClearingPartID = data_dict['ClearingPartID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.SequenceNo = data_dict['SequenceNo']
            self.TradeSource = chr(data_dict['TradeSource'])
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ExchangeID = ''
            self.TradeID = ''
            self.Direction = ''
            self.OrderSysID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.TradingRole = ''
            self.reserve1 = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.Price = 0.0
            self.Volume = 0
            self.TradeDate = ''
            self.TradeTime = ''
            self.TradeType = ''
            self.PriceSource = ''
            self.TraderID = ''
            self.OrderLocalID = ''
            self.ClearingPartID = ''
            self.BusinessUnit = ''
            self.SequenceNo = 0
            self.TradeSource = ''
            self.ExchangeInstID = ''

class CThostFtdcTradeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OrderRef = data_dict['OrderRef']
            self.UserID = data_dict['UserID']
            self.ExchangeID = data_dict['ExchangeID']
            self.TradeID = data_dict['TradeID']
            self.Direction = chr(data_dict['Direction'])
            self.OrderSysID = data_dict['OrderSysID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.TradingRole = chr(data_dict['TradingRole'])
            self.reserve2 = data_dict['reserve2']
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.Price = data_dict['Price']
            self.Volume = data_dict['Volume']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.TradeType = chr(data_dict['TradeType'])
            self.PriceSource = chr(data_dict['PriceSource'])
            self.TraderID = data_dict['TraderID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ClearingPartID = data_dict['ClearingPartID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.SequenceNo = data_dict['SequenceNo']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.BrokerOrderSeq = data_dict['BrokerOrderSeq']
            self.TradeSource = chr(data_dict['TradeSource'])
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OrderRef = ''
            self.UserID = ''
            self.ExchangeID = ''
            self.TradeID = ''
            self.Direction = ''
            self.OrderSysID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.TradingRole = ''
            self.reserve2 = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.Price = 0.0
            self.Volume = 0
            self.TradeDate = ''
            self.TradeTime = ''
            self.TradeType = ''
            self.PriceSource = ''
            self.TraderID = ''
            self.OrderLocalID = ''
            self.ClearingPartID = ''
            self.BusinessUnit = ''
            self.SequenceNo = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.BrokerOrderSeq = 0
            self.TradeSource = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''

class CThostFtdcUserSessionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.LoginDate = data_dict['LoginDate']
            self.LoginTime = data_dict['LoginTime']
            self.reserve1 = data_dict['reserve1']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.InterfaceProductInfo = data_dict['InterfaceProductInfo']
            self.ProtocolInfo = data_dict['ProtocolInfo']
            self.MacAddress = data_dict['MacAddress']
            self.LoginRemark = data_dict['LoginRemark']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.FrontID = 0
            self.SessionID = 0
            self.BrokerID = ''
            self.UserID = ''
            self.LoginDate = ''
            self.LoginTime = ''
            self.reserve1 = ''
            self.UserProductInfo = ''
            self.InterfaceProductInfo = ''
            self.ProtocolInfo = ''
            self.MacAddress = ''
            self.LoginRemark = ''
            self.IPAddress = ''

class CThostFtdcQryMaxOrderVolumeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.Direction = chr(data_dict['Direction'])
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.MaxVolume = data_dict['MaxVolume']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.Direction = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.MaxVolume = 0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcSettlementInfoConfirmField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ConfirmDate = data_dict['ConfirmDate']
            self.ConfirmTime = data_dict['ConfirmTime']
            self.SettlementID = data_dict['SettlementID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ConfirmDate = ''
            self.ConfirmTime = ''
            self.SettlementID = 0
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcSyncDepositField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.DepositSeqNo = data_dict['DepositSeqNo']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.Deposit = data_dict['Deposit']
            self.IsForce = data_dict['IsForce']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.DepositSeqNo = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.Deposit = 0.0
            self.IsForce = 0
            self.CurrencyID = ''

class CThostFtdcSyncFundMortgageField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.MortgageSeqNo = data_dict['MortgageSeqNo']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.FromCurrencyID = data_dict['FromCurrencyID']
            self.MortgageAmount = data_dict['MortgageAmount']
            self.ToCurrencyID = data_dict['ToCurrencyID']
        else:
            self.MortgageSeqNo = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.FromCurrencyID = ''
            self.MortgageAmount = 0.0
            self.ToCurrencyID = ''

class CThostFtdcBrokerSyncField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
        else:
            self.BrokerID = ''

class CThostFtdcSyncingInvestorField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InvestorID = data_dict['InvestorID']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorGroupID = data_dict['InvestorGroupID']
            self.InvestorName = data_dict['InvestorName']
            self.IdentifiedCardType = chr(data_dict['IdentifiedCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.IsActive = data_dict['IsActive']
            self.Telephone = data_dict['Telephone']
            self.Address = data_dict['Address']
            self.OpenDate = data_dict['OpenDate']
            self.Mobile = data_dict['Mobile']
            self.CommModelID = data_dict['CommModelID']
            self.MarginModelID = data_dict['MarginModelID']
        else:
            self.InvestorID = ''
            self.BrokerID = ''
            self.InvestorGroupID = ''
            self.InvestorName = ''
            self.IdentifiedCardType = ''
            self.IdentifiedCardNo = ''
            self.IsActive = 0
            self.Telephone = ''
            self.Address = ''
            self.OpenDate = ''
            self.Mobile = ''
            self.CommModelID = ''
            self.MarginModelID = ''

class CThostFtdcSyncingTradingCodeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InvestorID = data_dict['InvestorID']
            self.BrokerID = data_dict['BrokerID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ClientID = data_dict['ClientID']
            self.IsActive = data_dict['IsActive']
            self.ClientIDType = chr(data_dict['ClientIDType'])
        else:
            self.InvestorID = ''
            self.BrokerID = ''
            self.ExchangeID = ''
            self.ClientID = ''
            self.IsActive = 0
            self.ClientIDType = ''

class CThostFtdcSyncingInvestorGroupField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorGroupID = data_dict['InvestorGroupID']
            self.InvestorGroupName = data_dict['InvestorGroupName']
        else:
            self.BrokerID = ''
            self.InvestorGroupID = ''
            self.InvestorGroupName = ''

class CThostFtdcSyncingTradingAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.PreMortgage = data_dict['PreMortgage']
            self.PreCredit = data_dict['PreCredit']
            self.PreDeposit = data_dict['PreDeposit']
            self.PreBalance = data_dict['PreBalance']
            self.PreMargin = data_dict['PreMargin']
            self.InterestBase = data_dict['InterestBase']
            self.Interest = data_dict['Interest']
            self.Deposit = data_dict['Deposit']
            self.Withdraw = data_dict['Withdraw']
            self.FrozenMargin = data_dict['FrozenMargin']
            self.FrozenCash = data_dict['FrozenCash']
            self.FrozenCommission = data_dict['FrozenCommission']
            self.CurrMargin = data_dict['CurrMargin']
            self.CashIn = data_dict['CashIn']
            self.Commission = data_dict['Commission']
            self.CloseProfit = data_dict['CloseProfit']
            self.PositionProfit = data_dict['PositionProfit']
            self.Balance = data_dict['Balance']
            self.Available = data_dict['Available']
            self.WithdrawQuota = data_dict['WithdrawQuota']
            self.Reserve = data_dict['Reserve']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.Credit = data_dict['Credit']
            self.Mortgage = data_dict['Mortgage']
            self.ExchangeMargin = data_dict['ExchangeMargin']
            self.DeliveryMargin = data_dict['DeliveryMargin']
            self.ExchangeDeliveryMargin = data_dict['ExchangeDeliveryMargin']
            self.ReserveBalance = data_dict['ReserveBalance']
            self.CurrencyID = data_dict['CurrencyID']
            self.PreFundMortgageIn = data_dict['PreFundMortgageIn']
            self.PreFundMortgageOut = data_dict['PreFundMortgageOut']
            self.FundMortgageIn = data_dict['FundMortgageIn']
            self.FundMortgageOut = data_dict['FundMortgageOut']
            self.FundMortgageAvailable = data_dict['FundMortgageAvailable']
            self.MortgageableFund = data_dict['MortgageableFund']
            self.SpecProductMargin = data_dict['SpecProductMargin']
            self.SpecProductFrozenMargin = data_dict['SpecProductFrozenMargin']
            self.SpecProductCommission = data_dict['SpecProductCommission']
            self.SpecProductFrozenCommission = data_dict['SpecProductFrozenCommission']
            self.SpecProductPositionProfit = data_dict['SpecProductPositionProfit']
            self.SpecProductCloseProfit = data_dict['SpecProductCloseProfit']
            self.SpecProductPositionProfitByAlg = data_dict['SpecProductPositionProfitByAlg']
            self.SpecProductExchangeMargin = data_dict['SpecProductExchangeMargin']
            self.FrozenSwap = data_dict['FrozenSwap']
            self.RemainSwap = data_dict['RemainSwap']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.PreMortgage = 0.0
            self.PreCredit = 0.0
            self.PreDeposit = 0.0
            self.PreBalance = 0.0
            self.PreMargin = 0.0
            self.InterestBase = 0.0
            self.Interest = 0.0
            self.Deposit = 0.0
            self.Withdraw = 0.0
            self.FrozenMargin = 0.0
            self.FrozenCash = 0.0
            self.FrozenCommission = 0.0
            self.CurrMargin = 0.0
            self.CashIn = 0.0
            self.Commission = 0.0
            self.CloseProfit = 0.0
            self.PositionProfit = 0.0
            self.Balance = 0.0
            self.Available = 0.0
            self.WithdrawQuota = 0.0
            self.Reserve = 0.0
            self.TradingDay = ''
            self.SettlementID = 0
            self.Credit = 0.0
            self.Mortgage = 0.0
            self.ExchangeMargin = 0.0
            self.DeliveryMargin = 0.0
            self.ExchangeDeliveryMargin = 0.0
            self.ReserveBalance = 0.0
            self.CurrencyID = ''
            self.PreFundMortgageIn = 0.0
            self.PreFundMortgageOut = 0.0
            self.FundMortgageIn = 0.0
            self.FundMortgageOut = 0.0
            self.FundMortgageAvailable = 0.0
            self.MortgageableFund = 0.0
            self.SpecProductMargin = 0.0
            self.SpecProductFrozenMargin = 0.0
            self.SpecProductCommission = 0.0
            self.SpecProductFrozenCommission = 0.0
            self.SpecProductPositionProfit = 0.0
            self.SpecProductCloseProfit = 0.0
            self.SpecProductPositionProfitByAlg = 0.0
            self.SpecProductExchangeMargin = 0.0
            self.FrozenSwap = 0.0
            self.RemainSwap = 0.0

class CThostFtdcSyncingInvestorPositionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.PosiDirection = chr(data_dict['PosiDirection'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.PositionDate = chr(data_dict['PositionDate'])
            self.YdPosition = data_dict['YdPosition']
            self.Position = data_dict['Position']
            self.LongFrozen = data_dict['LongFrozen']
            self.ShortFrozen = data_dict['ShortFrozen']
            self.LongFrozenAmount = data_dict['LongFrozenAmount']
            self.ShortFrozenAmount = data_dict['ShortFrozenAmount']
            self.OpenVolume = data_dict['OpenVolume']
            self.CloseVolume = data_dict['CloseVolume']
            self.OpenAmount = data_dict['OpenAmount']
            self.CloseAmount = data_dict['CloseAmount']
            self.PositionCost = data_dict['PositionCost']
            self.PreMargin = data_dict['PreMargin']
            self.UseMargin = data_dict['UseMargin']
            self.FrozenMargin = data_dict['FrozenMargin']
            self.FrozenCash = data_dict['FrozenCash']
            self.FrozenCommission = data_dict['FrozenCommission']
            self.CashIn = data_dict['CashIn']
            self.Commission = data_dict['Commission']
            self.CloseProfit = data_dict['CloseProfit']
            self.PositionProfit = data_dict['PositionProfit']
            self.PreSettlementPrice = data_dict['PreSettlementPrice']
            self.SettlementPrice = data_dict['SettlementPrice']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OpenCost = data_dict['OpenCost']
            self.ExchangeMargin = data_dict['ExchangeMargin']
            self.CombPosition = data_dict['CombPosition']
            self.CombLongFrozen = data_dict['CombLongFrozen']
            self.CombShortFrozen = data_dict['CombShortFrozen']
            self.CloseProfitByDate = data_dict['CloseProfitByDate']
            self.CloseProfitByTrade = data_dict['CloseProfitByTrade']
            self.TodayPosition = data_dict['TodayPosition']
            self.MarginRateByMoney = data_dict['MarginRateByMoney']
            self.MarginRateByVolume = data_dict['MarginRateByVolume']
            self.StrikeFrozen = data_dict['StrikeFrozen']
            self.StrikeFrozenAmount = data_dict['StrikeFrozenAmount']
            self.AbandonFrozen = data_dict['AbandonFrozen']
            self.ExchangeID = data_dict['ExchangeID']
            self.YdStrikeFrozen = data_dict['YdStrikeFrozen']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.PositionCostOffset = data_dict['PositionCostOffset']
            self.TasPosition = data_dict['TasPosition']
            self.TasPositionCost = data_dict['TasPositionCost']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.PosiDirection = ''
            self.HedgeFlag = ''
            self.PositionDate = ''
            self.YdPosition = 0
            self.Position = 0
            self.LongFrozen = 0
            self.ShortFrozen = 0
            self.LongFrozenAmount = 0.0
            self.ShortFrozenAmount = 0.0
            self.OpenVolume = 0
            self.CloseVolume = 0
            self.OpenAmount = 0.0
            self.CloseAmount = 0.0
            self.PositionCost = 0.0
            self.PreMargin = 0.0
            self.UseMargin = 0.0
            self.FrozenMargin = 0.0
            self.FrozenCash = 0.0
            self.FrozenCommission = 0.0
            self.CashIn = 0.0
            self.Commission = 0.0
            self.CloseProfit = 0.0
            self.PositionProfit = 0.0
            self.PreSettlementPrice = 0.0
            self.SettlementPrice = 0.0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OpenCost = 0.0
            self.ExchangeMargin = 0.0
            self.CombPosition = 0
            self.CombLongFrozen = 0
            self.CombShortFrozen = 0
            self.CloseProfitByDate = 0.0
            self.CloseProfitByTrade = 0.0
            self.TodayPosition = 0
            self.MarginRateByMoney = 0.0
            self.MarginRateByVolume = 0.0
            self.StrikeFrozen = 0
            self.StrikeFrozenAmount = 0.0
            self.AbandonFrozen = 0
            self.ExchangeID = ''
            self.YdStrikeFrozen = 0
            self.InvestUnitID = ''
            self.PositionCostOffset = 0.0
            self.TasPosition = 0
            self.TasPositionCost = 0.0
            self.InstrumentID = ''

class CThostFtdcSyncingInstrumentMarginRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.LongMarginRatioByMoney = data_dict['LongMarginRatioByMoney']
            self.LongMarginRatioByVolume = data_dict['LongMarginRatioByVolume']
            self.ShortMarginRatioByMoney = data_dict['ShortMarginRatioByMoney']
            self.ShortMarginRatioByVolume = data_dict['ShortMarginRatioByVolume']
            self.IsRelative = data_dict['IsRelative']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.HedgeFlag = ''
            self.LongMarginRatioByMoney = 0.0
            self.LongMarginRatioByVolume = 0.0
            self.ShortMarginRatioByMoney = 0.0
            self.ShortMarginRatioByVolume = 0.0
            self.IsRelative = 0
            self.InstrumentID = ''

class CThostFtdcSyncingInstrumentCommissionRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OpenRatioByMoney = data_dict['OpenRatioByMoney']
            self.OpenRatioByVolume = data_dict['OpenRatioByVolume']
            self.CloseRatioByMoney = data_dict['CloseRatioByMoney']
            self.CloseRatioByVolume = data_dict['CloseRatioByVolume']
            self.CloseTodayRatioByMoney = data_dict['CloseTodayRatioByMoney']
            self.CloseTodayRatioByVolume = data_dict['CloseTodayRatioByVolume']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.OpenRatioByMoney = 0.0
            self.OpenRatioByVolume = 0.0
            self.CloseRatioByMoney = 0.0
            self.CloseRatioByVolume = 0.0
            self.CloseTodayRatioByMoney = 0.0
            self.CloseTodayRatioByVolume = 0.0
            self.InstrumentID = ''

class CThostFtdcSyncingInstrumentTradingRightField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.TradingRight = chr(data_dict['TradingRight'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.TradingRight = ''
            self.InstrumentID = ''

class CThostFtdcQryOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.InsertTimeStart = data_dict['InsertTimeStart']
            self.InsertTimeEnd = data_dict['InsertTimeEnd']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.InsertTimeStart = ''
            self.InsertTimeEnd = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryTradeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.TradeID = data_dict['TradeID']
            self.TradeTimeStart = data_dict['TradeTimeStart']
            self.TradeTimeEnd = data_dict['TradeTimeEnd']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.TradeID = ''
            self.TradeTimeStart = ''
            self.TradeTimeEnd = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryInvestorPositionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryTradingAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.CurrencyID = data_dict['CurrencyID']
            self.BizType = chr(data_dict['BizType'])
            self.AccountID = data_dict['AccountID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.CurrencyID = ''
            self.BizType = ''
            self.AccountID = ''

class CThostFtdcQryInvestorField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcQryTradingCodeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ClientID = data_dict['ClientID']
            self.ClientIDType = chr(data_dict['ClientIDType'])
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''
            self.ClientID = ''
            self.ClientIDType = ''
            self.InvestUnitID = ''

class CThostFtdcQryInvestorGroupField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
        else:
            self.BrokerID = ''

class CThostFtdcQryInstrumentMarginRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryInstrumentCommissionRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryInstrumentTradingRightField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcQryBrokerField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
        else:
            self.BrokerID = ''

class CThostFtdcQryTraderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.TraderID = data_dict['TraderID']
        else:
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.TraderID = ''

class CThostFtdcQrySuperUserFunctionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.UserID = data_dict['UserID']
        else:
            self.UserID = ''

class CThostFtdcQryUserSessionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.FrontID = 0
            self.SessionID = 0
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcQryPartBrokerField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.BrokerID = data_dict['BrokerID']
            self.ParticipantID = data_dict['ParticipantID']
        else:
            self.ExchangeID = ''
            self.BrokerID = ''
            self.ParticipantID = ''

class CThostFtdcQryFrontStatusField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontID = data_dict['FrontID']
        else:
            self.FrontID = 0

class CThostFtdcQryExchangeOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.TraderID = ''
            self.ExchangeInstID = ''

class CThostFtdcQryOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''

class CThostFtdcQryExchangeOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.ExchangeID = ''
            self.TraderID = ''

class CThostFtdcQrySuperUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.UserID = data_dict['UserID']
        else:
            self.UserID = ''

class CThostFtdcQryExchangeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.ExchangeID = ''

class CThostFtdcQryProductField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ProductClass = chr(data_dict['ProductClass'])
            self.ExchangeID = data_dict['ExchangeID']
            self.ProductID = data_dict['ProductID']
        else:
            self.reserve1 = ''
            self.ProductClass = ''
            self.ExchangeID = ''
            self.ProductID = ''

class CThostFtdcQryInstrumentField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve2 = data_dict['reserve2']
            self.reserve3 = data_dict['reserve3']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.ProductID = data_dict['ProductID']
        else:
            self.reserve1 = ''
            self.ExchangeID = ''
            self.reserve2 = ''
            self.reserve3 = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.ProductID = ''

class CThostFtdcQryDepthMarketDataField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcQryBrokerUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcQryBrokerUserFunctionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcQryTraderOfferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.TraderID = data_dict['TraderID']
        else:
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.TraderID = ''

class CThostFtdcQrySyncDepositField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.DepositSeqNo = data_dict['DepositSeqNo']
        else:
            self.BrokerID = ''
            self.DepositSeqNo = ''

class CThostFtdcQrySettlementInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.TradingDay = data_dict['TradingDay']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.TradingDay = ''
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcQryExchangeMarginRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcQryExchangeMarginRateAdjustField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.InstrumentID = ''

class CThostFtdcQryExchangeRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.FromCurrencyID = data_dict['FromCurrencyID']
            self.ToCurrencyID = data_dict['ToCurrencyID']
        else:
            self.BrokerID = ''
            self.FromCurrencyID = ''
            self.ToCurrencyID = ''

class CThostFtdcQrySyncFundMortgageField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.MortgageSeqNo = data_dict['MortgageSeqNo']
        else:
            self.BrokerID = ''
            self.MortgageSeqNo = ''

class CThostFtdcQryHisOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.InsertTimeStart = data_dict['InsertTimeStart']
            self.InsertTimeEnd = data_dict['InsertTimeEnd']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.InsertTimeStart = ''
            self.InsertTimeEnd = ''
            self.TradingDay = ''
            self.SettlementID = 0
            self.InstrumentID = ''

class CThostFtdcOptionInstrMiniMarginField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.MinMargin = data_dict['MinMargin']
            self.ValueMethod = chr(data_dict['ValueMethod'])
            self.IsRelative = data_dict['IsRelative']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.MinMargin = 0.0
            self.ValueMethod = ''
            self.IsRelative = 0
            self.InstrumentID = ''

class CThostFtdcOptionInstrMarginAdjustField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.SShortMarginRatioByMoney = data_dict['SShortMarginRatioByMoney']
            self.SShortMarginRatioByVolume = data_dict['SShortMarginRatioByVolume']
            self.HShortMarginRatioByMoney = data_dict['HShortMarginRatioByMoney']
            self.HShortMarginRatioByVolume = data_dict['HShortMarginRatioByVolume']
            self.AShortMarginRatioByMoney = data_dict['AShortMarginRatioByMoney']
            self.AShortMarginRatioByVolume = data_dict['AShortMarginRatioByVolume']
            self.IsRelative = data_dict['IsRelative']
            self.MShortMarginRatioByMoney = data_dict['MShortMarginRatioByMoney']
            self.MShortMarginRatioByVolume = data_dict['MShortMarginRatioByVolume']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.SShortMarginRatioByMoney = 0.0
            self.SShortMarginRatioByVolume = 0.0
            self.HShortMarginRatioByMoney = 0.0
            self.HShortMarginRatioByVolume = 0.0
            self.AShortMarginRatioByMoney = 0.0
            self.AShortMarginRatioByVolume = 0.0
            self.IsRelative = 0
            self.MShortMarginRatioByMoney = 0.0
            self.MShortMarginRatioByVolume = 0.0
            self.InstrumentID = ''

class CThostFtdcOptionInstrCommRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OpenRatioByMoney = data_dict['OpenRatioByMoney']
            self.OpenRatioByVolume = data_dict['OpenRatioByVolume']
            self.CloseRatioByMoney = data_dict['CloseRatioByMoney']
            self.CloseRatioByVolume = data_dict['CloseRatioByVolume']
            self.CloseTodayRatioByMoney = data_dict['CloseTodayRatioByMoney']
            self.CloseTodayRatioByVolume = data_dict['CloseTodayRatioByVolume']
            self.StrikeRatioByMoney = data_dict['StrikeRatioByMoney']
            self.StrikeRatioByVolume = data_dict['StrikeRatioByVolume']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.OpenRatioByMoney = 0.0
            self.OpenRatioByVolume = 0.0
            self.CloseRatioByMoney = 0.0
            self.CloseRatioByVolume = 0.0
            self.CloseTodayRatioByMoney = 0.0
            self.CloseTodayRatioByVolume = 0.0
            self.StrikeRatioByMoney = 0.0
            self.StrikeRatioByVolume = 0.0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcOptionInstrTradeCostField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.FixedMargin = data_dict['FixedMargin']
            self.MiniMargin = data_dict['MiniMargin']
            self.Royalty = data_dict['Royalty']
            self.ExchFixedMargin = data_dict['ExchFixedMargin']
            self.ExchMiniMargin = data_dict['ExchMiniMargin']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.FixedMargin = 0.0
            self.MiniMargin = 0.0
            self.Royalty = 0.0
            self.ExchFixedMargin = 0.0
            self.ExchMiniMargin = 0.0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryOptionInstrTradeCostField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.InputPrice = data_dict['InputPrice']
            self.UnderlyingPrice = data_dict['UnderlyingPrice']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.InputPrice = 0.0
            self.UnderlyingPrice = 0.0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryOptionInstrCommRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcIndexPriceField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.ClosePrice = data_dict['ClosePrice']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.ClosePrice = 0.0
            self.InstrumentID = ''

class CThostFtdcInputExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExecOrderRef = data_dict['ExecOrderRef']
            self.UserID = data_dict['UserID']
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ActionType = chr(data_dict['ActionType'])
            self.PosiDirection = chr(data_dict['PosiDirection'])
            self.ReservePositionFlag = chr(data_dict['ReservePositionFlag'])
            self.CloseFlag = chr(data_dict['CloseFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExecOrderRef = ''
            self.UserID = ''
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.ActionType = ''
            self.PosiDirection = ''
            self.ReservePositionFlag = ''
            self.CloseFlag = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcInputExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExecOrderActionRef = data_dict['ExecOrderActionRef']
            self.ExecOrderRef = data_dict['ExecOrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExecOrderActionRef = 0
            self.ExecOrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.ExecOrderSysID = ''
            self.ActionFlag = ''
            self.UserID = ''
            self.reserve1 = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExecOrderRef = data_dict['ExecOrderRef']
            self.UserID = data_dict['UserID']
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ActionType = chr(data_dict['ActionType'])
            self.PosiDirection = chr(data_dict['PosiDirection'])
            self.ReservePositionFlag = chr(data_dict['ReservePositionFlag'])
            self.CloseFlag = chr(data_dict['CloseFlag'])
            self.ExecOrderLocalID = data_dict['ExecOrderLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.CancelTime = data_dict['CancelTime']
            self.ExecResult = chr(data_dict['ExecResult'])
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.StatusMsg = data_dict['StatusMsg']
            self.ActiveUserID = data_dict['ActiveUserID']
            self.BrokerExecOrderSeq = data_dict['BrokerExecOrderSeq']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExecOrderRef = ''
            self.UserID = ''
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.ActionType = ''
            self.PosiDirection = ''
            self.ReservePositionFlag = ''
            self.CloseFlag = ''
            self.ExecOrderLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.ExecOrderSysID = ''
            self.InsertDate = ''
            self.InsertTime = ''
            self.CancelTime = ''
            self.ExecResult = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.FrontID = 0
            self.SessionID = 0
            self.UserProductInfo = ''
            self.StatusMsg = ''
            self.ActiveUserID = ''
            self.BrokerExecOrderSeq = 0
            self.BranchID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExecOrderActionRef = data_dict['ExecOrderActionRef']
            self.ExecOrderRef = data_dict['ExecOrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.ExecOrderLocalID = data_dict['ExecOrderLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.ActionType = chr(data_dict['ActionType'])
            self.StatusMsg = data_dict['StatusMsg']
            self.reserve1 = data_dict['reserve1']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExecOrderActionRef = 0
            self.ExecOrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.ExecOrderSysID = ''
            self.ActionFlag = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.ExecOrderLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.ActionType = ''
            self.StatusMsg = ''
            self.reserve1 = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.InsertTimeStart = data_dict['InsertTimeStart']
            self.InsertTimeEnd = data_dict['InsertTimeEnd']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.ExecOrderSysID = ''
            self.InsertTimeStart = ''
            self.InsertTimeEnd = ''
            self.InstrumentID = ''

class CThostFtdcExchangeExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ActionType = chr(data_dict['ActionType'])
            self.PosiDirection = chr(data_dict['PosiDirection'])
            self.ReservePositionFlag = chr(data_dict['ReservePositionFlag'])
            self.CloseFlag = chr(data_dict['CloseFlag'])
            self.ExecOrderLocalID = data_dict['ExecOrderLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.CancelTime = data_dict['CancelTime']
            self.ExecResult = chr(data_dict['ExecResult'])
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.BranchID = data_dict['BranchID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.ActionType = ''
            self.PosiDirection = ''
            self.ReservePositionFlag = ''
            self.CloseFlag = ''
            self.ExecOrderLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.ExecOrderSysID = ''
            self.InsertDate = ''
            self.InsertTime = ''
            self.CancelTime = ''
            self.ExecResult = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.BranchID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryExchangeExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.TraderID = ''
            self.ExchangeInstID = ''

class CThostFtdcQryExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''

class CThostFtdcExchangeExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.ExecOrderLocalID = data_dict['ExecOrderLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.ActionType = chr(data_dict['ActionType'])
            self.BranchID = data_dict['BranchID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.reserve2 = data_dict['reserve2']
            self.Volume = data_dict['Volume']
            self.IPAddress = data_dict['IPAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ExchangeID = ''
            self.ExecOrderSysID = ''
            self.ActionFlag = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.ExecOrderLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.ActionType = ''
            self.BranchID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.reserve2 = ''
            self.Volume = 0
            self.IPAddress = ''
            self.ExchangeInstID = ''

class CThostFtdcQryExchangeExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.ExchangeID = ''
            self.TraderID = ''

class CThostFtdcErrExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExecOrderRef = data_dict['ExecOrderRef']
            self.UserID = data_dict['UserID']
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ActionType = chr(data_dict['ActionType'])
            self.PosiDirection = chr(data_dict['PosiDirection'])
            self.ReservePositionFlag = chr(data_dict['ReservePositionFlag'])
            self.CloseFlag = chr(data_dict['CloseFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExecOrderRef = ''
            self.UserID = ''
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.ActionType = ''
            self.PosiDirection = ''
            self.ReservePositionFlag = ''
            self.CloseFlag = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryErrExecOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcErrExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExecOrderActionRef = data_dict['ExecOrderActionRef']
            self.ExecOrderRef = data_dict['ExecOrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ExecOrderSysID = data_dict['ExecOrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExecOrderActionRef = 0
            self.ExecOrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.ExecOrderSysID = ''
            self.ActionFlag = ''
            self.UserID = ''
            self.reserve1 = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryErrExecOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcOptionInstrTradingRightField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.Direction = chr(data_dict['Direction'])
            self.TradingRight = chr(data_dict['TradingRight'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.Direction = ''
            self.TradingRight = ''
            self.InstrumentID = ''

class CThostFtdcQryOptionInstrTradingRightField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.Direction = chr(data_dict['Direction'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.Direction = ''
            self.InstrumentID = ''

class CThostFtdcInputForQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ForQuoteRef = data_dict['ForQuoteRef']
            self.UserID = data_dict['UserID']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ForQuoteRef = ''
            self.UserID = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcForQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ForQuoteRef = data_dict['ForQuoteRef']
            self.UserID = data_dict['UserID']
            self.ForQuoteLocalID = data_dict['ForQuoteLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.ForQuoteStatus = chr(data_dict['ForQuoteStatus'])
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.StatusMsg = data_dict['StatusMsg']
            self.ActiveUserID = data_dict['ActiveUserID']
            self.BrokerForQutoSeq = data_dict['BrokerForQutoSeq']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ForQuoteRef = ''
            self.UserID = ''
            self.ForQuoteLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.InsertDate = ''
            self.InsertTime = ''
            self.ForQuoteStatus = ''
            self.FrontID = 0
            self.SessionID = 0
            self.StatusMsg = ''
            self.ActiveUserID = ''
            self.BrokerForQutoSeq = 0
            self.InvestUnitID = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryForQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InsertTimeStart = data_dict['InsertTimeStart']
            self.InsertTimeEnd = data_dict['InsertTimeEnd']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InsertTimeStart = ''
            self.InsertTimeEnd = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcExchangeForQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ForQuoteLocalID = data_dict['ForQuoteLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.ForQuoteStatus = chr(data_dict['ForQuoteStatus'])
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.ForQuoteLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.InsertDate = ''
            self.InsertTime = ''
            self.ForQuoteStatus = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryExchangeForQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.TraderID = ''
            self.ExchangeInstID = ''

class CThostFtdcInputQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.QuoteRef = data_dict['QuoteRef']
            self.UserID = data_dict['UserID']
            self.AskPrice = data_dict['AskPrice']
            self.BidPrice = data_dict['BidPrice']
            self.AskVolume = data_dict['AskVolume']
            self.BidVolume = data_dict['BidVolume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.AskOffsetFlag = chr(data_dict['AskOffsetFlag'])
            self.BidOffsetFlag = chr(data_dict['BidOffsetFlag'])
            self.AskHedgeFlag = chr(data_dict['AskHedgeFlag'])
            self.BidHedgeFlag = chr(data_dict['BidHedgeFlag'])
            self.AskOrderRef = data_dict['AskOrderRef']
            self.BidOrderRef = data_dict['BidOrderRef']
            self.ForQuoteSysID = data_dict['ForQuoteSysID']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.QuoteRef = ''
            self.UserID = ''
            self.AskPrice = 0.0
            self.BidPrice = 0.0
            self.AskVolume = 0
            self.BidVolume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.AskOffsetFlag = ''
            self.BidOffsetFlag = ''
            self.AskHedgeFlag = ''
            self.BidHedgeFlag = ''
            self.AskOrderRef = ''
            self.BidOrderRef = ''
            self.ForQuoteSysID = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcInputQuoteActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.QuoteActionRef = data_dict['QuoteActionRef']
            self.QuoteRef = data_dict['QuoteRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.QuoteSysID = data_dict['QuoteSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.QuoteActionRef = 0
            self.QuoteRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.QuoteSysID = ''
            self.ActionFlag = ''
            self.UserID = ''
            self.reserve1 = ''
            self.InvestUnitID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.QuoteRef = data_dict['QuoteRef']
            self.UserID = data_dict['UserID']
            self.AskPrice = data_dict['AskPrice']
            self.BidPrice = data_dict['BidPrice']
            self.AskVolume = data_dict['AskVolume']
            self.BidVolume = data_dict['BidVolume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.AskOffsetFlag = chr(data_dict['AskOffsetFlag'])
            self.BidOffsetFlag = chr(data_dict['BidOffsetFlag'])
            self.AskHedgeFlag = chr(data_dict['AskHedgeFlag'])
            self.BidHedgeFlag = chr(data_dict['BidHedgeFlag'])
            self.QuoteLocalID = data_dict['QuoteLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.NotifySequence = data_dict['NotifySequence']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.QuoteSysID = data_dict['QuoteSysID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.CancelTime = data_dict['CancelTime']
            self.QuoteStatus = chr(data_dict['QuoteStatus'])
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.AskOrderSysID = data_dict['AskOrderSysID']
            self.BidOrderSysID = data_dict['BidOrderSysID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.StatusMsg = data_dict['StatusMsg']
            self.ActiveUserID = data_dict['ActiveUserID']
            self.BrokerQuoteSeq = data_dict['BrokerQuoteSeq']
            self.AskOrderRef = data_dict['AskOrderRef']
            self.BidOrderRef = data_dict['BidOrderRef']
            self.ForQuoteSysID = data_dict['ForQuoteSysID']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.QuoteRef = ''
            self.UserID = ''
            self.AskPrice = 0.0
            self.BidPrice = 0.0
            self.AskVolume = 0
            self.BidVolume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.AskOffsetFlag = ''
            self.BidOffsetFlag = ''
            self.AskHedgeFlag = ''
            self.BidHedgeFlag = ''
            self.QuoteLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.NotifySequence = 0
            self.OrderSubmitStatus = ''
            self.TradingDay = ''
            self.SettlementID = 0
            self.QuoteSysID = ''
            self.InsertDate = ''
            self.InsertTime = ''
            self.CancelTime = ''
            self.QuoteStatus = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.AskOrderSysID = ''
            self.BidOrderSysID = ''
            self.FrontID = 0
            self.SessionID = 0
            self.UserProductInfo = ''
            self.StatusMsg = ''
            self.ActiveUserID = ''
            self.BrokerQuoteSeq = 0
            self.AskOrderRef = ''
            self.BidOrderRef = ''
            self.ForQuoteSysID = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQuoteActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.QuoteActionRef = data_dict['QuoteActionRef']
            self.QuoteRef = data_dict['QuoteRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.QuoteSysID = data_dict['QuoteSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.QuoteLocalID = data_dict['QuoteLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.StatusMsg = data_dict['StatusMsg']
            self.reserve1 = data_dict['reserve1']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.QuoteActionRef = 0
            self.QuoteRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.QuoteSysID = ''
            self.ActionFlag = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.QuoteLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.StatusMsg = ''
            self.reserve1 = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.QuoteSysID = data_dict['QuoteSysID']
            self.InsertTimeStart = data_dict['InsertTimeStart']
            self.InsertTimeEnd = data_dict['InsertTimeEnd']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.QuoteSysID = ''
            self.InsertTimeStart = ''
            self.InsertTimeEnd = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcExchangeQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.AskPrice = data_dict['AskPrice']
            self.BidPrice = data_dict['BidPrice']
            self.AskVolume = data_dict['AskVolume']
            self.BidVolume = data_dict['BidVolume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.AskOffsetFlag = chr(data_dict['AskOffsetFlag'])
            self.BidOffsetFlag = chr(data_dict['BidOffsetFlag'])
            self.AskHedgeFlag = chr(data_dict['AskHedgeFlag'])
            self.BidHedgeFlag = chr(data_dict['BidHedgeFlag'])
            self.QuoteLocalID = data_dict['QuoteLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.NotifySequence = data_dict['NotifySequence']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.QuoteSysID = data_dict['QuoteSysID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.CancelTime = data_dict['CancelTime']
            self.QuoteStatus = chr(data_dict['QuoteStatus'])
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.AskOrderSysID = data_dict['AskOrderSysID']
            self.BidOrderSysID = data_dict['BidOrderSysID']
            self.ForQuoteSysID = data_dict['ForQuoteSysID']
            self.BranchID = data_dict['BranchID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.AskPrice = 0.0
            self.BidPrice = 0.0
            self.AskVolume = 0
            self.BidVolume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.AskOffsetFlag = ''
            self.BidOffsetFlag = ''
            self.AskHedgeFlag = ''
            self.BidHedgeFlag = ''
            self.QuoteLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.NotifySequence = 0
            self.OrderSubmitStatus = ''
            self.TradingDay = ''
            self.SettlementID = 0
            self.QuoteSysID = ''
            self.InsertDate = ''
            self.InsertTime = ''
            self.CancelTime = ''
            self.QuoteStatus = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.AskOrderSysID = ''
            self.BidOrderSysID = ''
            self.ForQuoteSysID = ''
            self.BranchID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryExchangeQuoteField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.TraderID = ''
            self.ExchangeInstID = ''

class CThostFtdcQryQuoteActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''

class CThostFtdcExchangeQuoteActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.QuoteSysID = data_dict['QuoteSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.QuoteLocalID = data_dict['QuoteLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.ExchangeID = ''
            self.QuoteSysID = ''
            self.ActionFlag = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.QuoteLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.IPAddress = ''

class CThostFtdcQryExchangeQuoteActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.ExchangeID = ''
            self.TraderID = ''

class CThostFtdcOptionInstrDeltaField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.Delta = data_dict['Delta']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.Delta = 0.0
            self.InstrumentID = ''

class CThostFtdcForQuoteRspField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.reserve1 = data_dict['reserve1']
            self.ForQuoteSysID = data_dict['ForQuoteSysID']
            self.ForQuoteTime = data_dict['ForQuoteTime']
            self.ActionDay = data_dict['ActionDay']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.TradingDay = ''
            self.reserve1 = ''
            self.ForQuoteSysID = ''
            self.ForQuoteTime = ''
            self.ActionDay = ''
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcStrikeOffsetField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.Offset = data_dict['Offset']
            self.OffsetType = chr(data_dict['OffsetType'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.Offset = 0.0
            self.OffsetType = ''
            self.InstrumentID = ''

class CThostFtdcQryStrikeOffsetField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcInputBatchOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OrderActionRef = data_dict['OrderActionRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.UserID = data_dict['UserID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OrderActionRef = 0
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.UserID = ''
            self.InvestUnitID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.IPAddress = ''

class CThostFtdcBatchOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OrderActionRef = data_dict['OrderActionRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.StatusMsg = data_dict['StatusMsg']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OrderActionRef = 0
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.StatusMsg = ''
            self.InvestUnitID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.IPAddress = ''

class CThostFtdcExchangeBatchOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.ExchangeID = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.IPAddress = ''

class CThostFtdcQryBatchOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''

class CThostFtdcCombInstrumentGuardField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.GuarantRatio = data_dict['GuarantRatio']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.GuarantRatio = 0.0
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcQryCombInstrumentGuardField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcInputCombActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.CombActionRef = data_dict['CombActionRef']
            self.UserID = data_dict['UserID']
            self.Direction = chr(data_dict['Direction'])
            self.Volume = data_dict['Volume']
            self.CombDirection = chr(data_dict['CombDirection'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.CombActionRef = ''
            self.UserID = ''
            self.Direction = ''
            self.Volume = 0
            self.CombDirection = ''
            self.HedgeFlag = ''
            self.ExchangeID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InvestUnitID = ''
            self.FrontID = 0
            self.SessionID = 0
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcCombActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.CombActionRef = data_dict['CombActionRef']
            self.UserID = data_dict['UserID']
            self.Direction = chr(data_dict['Direction'])
            self.Volume = data_dict['Volume']
            self.CombDirection = chr(data_dict['CombDirection'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.ActionStatus = chr(data_dict['ActionStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.SequenceNo = data_dict['SequenceNo']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.StatusMsg = data_dict['StatusMsg']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.ComTradeID = data_dict['ComTradeID']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.CombActionRef = ''
            self.UserID = ''
            self.Direction = ''
            self.Volume = 0
            self.CombDirection = ''
            self.HedgeFlag = ''
            self.ActionLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.ActionStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.SequenceNo = 0
            self.FrontID = 0
            self.SessionID = 0
            self.UserProductInfo = ''
            self.StatusMsg = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.ComTradeID = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryCombActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcExchangeCombActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.Direction = chr(data_dict['Direction'])
            self.Volume = data_dict['Volume']
            self.CombDirection = chr(data_dict['CombDirection'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.ActionStatus = chr(data_dict['ActionStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.SequenceNo = data_dict['SequenceNo']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ComTradeID = data_dict['ComTradeID']
            self.BranchID = data_dict['BranchID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.Direction = ''
            self.Volume = 0
            self.CombDirection = ''
            self.HedgeFlag = ''
            self.ActionLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.ActionStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.SequenceNo = 0
            self.reserve2 = ''
            self.MacAddress = ''
            self.ComTradeID = ''
            self.BranchID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryExchangeCombActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.TraderID = ''
            self.ExchangeInstID = ''

class CThostFtdcProductExchRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.QuoteCurrencyID = data_dict['QuoteCurrencyID']
            self.ExchangeRate = data_dict['ExchangeRate']
            self.ExchangeID = data_dict['ExchangeID']
            self.ProductID = data_dict['ProductID']
        else:
            self.reserve1 = ''
            self.QuoteCurrencyID = ''
            self.ExchangeRate = 0.0
            self.ExchangeID = ''
            self.ProductID = ''

class CThostFtdcQryProductExchRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.ProductID = data_dict['ProductID']
        else:
            self.reserve1 = ''
            self.ExchangeID = ''
            self.ProductID = ''

class CThostFtdcQryForQuoteParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcForQuoteParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.LastPrice = data_dict['LastPrice']
            self.PriceInterval = data_dict['PriceInterval']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.LastPrice = 0.0
            self.PriceInterval = 0.0
            self.InstrumentID = ''

class CThostFtdcMMOptionInstrCommRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OpenRatioByMoney = data_dict['OpenRatioByMoney']
            self.OpenRatioByVolume = data_dict['OpenRatioByVolume']
            self.CloseRatioByMoney = data_dict['CloseRatioByMoney']
            self.CloseRatioByVolume = data_dict['CloseRatioByVolume']
            self.CloseTodayRatioByMoney = data_dict['CloseTodayRatioByMoney']
            self.CloseTodayRatioByVolume = data_dict['CloseTodayRatioByVolume']
            self.StrikeRatioByMoney = data_dict['StrikeRatioByMoney']
            self.StrikeRatioByVolume = data_dict['StrikeRatioByVolume']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.OpenRatioByMoney = 0.0
            self.OpenRatioByVolume = 0.0
            self.CloseRatioByMoney = 0.0
            self.CloseRatioByVolume = 0.0
            self.CloseTodayRatioByMoney = 0.0
            self.CloseTodayRatioByVolume = 0.0
            self.StrikeRatioByMoney = 0.0
            self.StrikeRatioByVolume = 0.0
            self.InstrumentID = ''

class CThostFtdcQryMMOptionInstrCommRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcMMInstrumentCommissionRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OpenRatioByMoney = data_dict['OpenRatioByMoney']
            self.OpenRatioByVolume = data_dict['OpenRatioByVolume']
            self.CloseRatioByMoney = data_dict['CloseRatioByMoney']
            self.CloseRatioByVolume = data_dict['CloseRatioByVolume']
            self.CloseTodayRatioByMoney = data_dict['CloseTodayRatioByMoney']
            self.CloseTodayRatioByVolume = data_dict['CloseTodayRatioByVolume']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.OpenRatioByMoney = 0.0
            self.OpenRatioByVolume = 0.0
            self.CloseRatioByMoney = 0.0
            self.CloseRatioByVolume = 0.0
            self.CloseTodayRatioByMoney = 0.0
            self.CloseTodayRatioByVolume = 0.0
            self.InstrumentID = ''

class CThostFtdcQryMMInstrumentCommissionRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcInstrumentOrderCommRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.OrderCommByVolume = data_dict['OrderCommByVolume']
            self.OrderActionCommByVolume = data_dict['OrderActionCommByVolume']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.HedgeFlag = ''
            self.OrderCommByVolume = 0.0
            self.OrderActionCommByVolume = 0.0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryInstrumentOrderCommRateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcTradeParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.TradeParamID = chr(data_dict['TradeParamID'])
            self.TradeParamValue = data_dict['TradeParamValue']
            self.Memo = data_dict['Memo']
        else:
            self.BrokerID = ''
            self.TradeParamID = ''
            self.TradeParamValue = ''
            self.Memo = ''

class CThostFtdcInstrumentMarginRateULField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.LongMarginRatioByMoney = data_dict['LongMarginRatioByMoney']
            self.LongMarginRatioByVolume = data_dict['LongMarginRatioByVolume']
            self.ShortMarginRatioByMoney = data_dict['ShortMarginRatioByMoney']
            self.ShortMarginRatioByVolume = data_dict['ShortMarginRatioByVolume']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.HedgeFlag = ''
            self.LongMarginRatioByMoney = 0.0
            self.LongMarginRatioByVolume = 0.0
            self.ShortMarginRatioByMoney = 0.0
            self.ShortMarginRatioByVolume = 0.0
            self.InstrumentID = ''

class CThostFtdcFutureLimitPosiParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.SpecOpenVolume = data_dict['SpecOpenVolume']
            self.ArbiOpenVolume = data_dict['ArbiOpenVolume']
            self.OpenVolume = data_dict['OpenVolume']
            self.ProductID = data_dict['ProductID']
        else:
            self.InvestorRange = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.SpecOpenVolume = 0
            self.ArbiOpenVolume = 0
            self.OpenVolume = 0
            self.ProductID = ''

class CThostFtdcLoginForbiddenIPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.reserve1 = ''
            self.IPAddress = ''

class CThostFtdcIPListField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.IsWhite = data_dict['IsWhite']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.reserve1 = ''
            self.IsWhite = 0
            self.IPAddress = ''

class CThostFtdcInputOptionSelfCloseField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OptionSelfCloseRef = data_dict['OptionSelfCloseRef']
            self.UserID = data_dict['UserID']
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.OptSelfCloseFlag = chr(data_dict['OptSelfCloseFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OptionSelfCloseRef = ''
            self.UserID = ''
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.HedgeFlag = ''
            self.OptSelfCloseFlag = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcInputOptionSelfCloseActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OptionSelfCloseActionRef = data_dict['OptionSelfCloseActionRef']
            self.OptionSelfCloseRef = data_dict['OptionSelfCloseRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.OptionSelfCloseSysID = data_dict['OptionSelfCloseSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OptionSelfCloseActionRef = 0
            self.OptionSelfCloseRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.OptionSelfCloseSysID = ''
            self.ActionFlag = ''
            self.UserID = ''
            self.reserve1 = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcOptionSelfCloseField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OptionSelfCloseRef = data_dict['OptionSelfCloseRef']
            self.UserID = data_dict['UserID']
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.OptSelfCloseFlag = chr(data_dict['OptSelfCloseFlag'])
            self.OptionSelfCloseLocalID = data_dict['OptionSelfCloseLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OptionSelfCloseSysID = data_dict['OptionSelfCloseSysID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.CancelTime = data_dict['CancelTime']
            self.ExecResult = chr(data_dict['ExecResult'])
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.StatusMsg = data_dict['StatusMsg']
            self.ActiveUserID = data_dict['ActiveUserID']
            self.BrokerOptionSelfCloseSeq = data_dict['BrokerOptionSelfCloseSeq']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OptionSelfCloseRef = ''
            self.UserID = ''
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.HedgeFlag = ''
            self.OptSelfCloseFlag = ''
            self.OptionSelfCloseLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OptionSelfCloseSysID = ''
            self.InsertDate = ''
            self.InsertTime = ''
            self.CancelTime = ''
            self.ExecResult = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.FrontID = 0
            self.SessionID = 0
            self.UserProductInfo = ''
            self.StatusMsg = ''
            self.ActiveUserID = ''
            self.BrokerOptionSelfCloseSeq = 0
            self.BranchID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcOptionSelfCloseActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OptionSelfCloseActionRef = data_dict['OptionSelfCloseActionRef']
            self.OptionSelfCloseRef = data_dict['OptionSelfCloseRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.OptionSelfCloseSysID = data_dict['OptionSelfCloseSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OptionSelfCloseLocalID = data_dict['OptionSelfCloseLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.StatusMsg = data_dict['StatusMsg']
            self.reserve1 = data_dict['reserve1']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OptionSelfCloseActionRef = 0
            self.OptionSelfCloseRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.OptionSelfCloseSysID = ''
            self.ActionFlag = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OptionSelfCloseLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.StatusMsg = ''
            self.reserve1 = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryOptionSelfCloseField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.OptionSelfCloseSysID = data_dict['OptionSelfCloseSysID']
            self.InsertTimeStart = data_dict['InsertTimeStart']
            self.InsertTimeEnd = data_dict['InsertTimeEnd']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.OptionSelfCloseSysID = ''
            self.InsertTimeStart = ''
            self.InsertTimeEnd = ''
            self.InstrumentID = ''

class CThostFtdcExchangeOptionSelfCloseField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.Volume = data_dict['Volume']
            self.RequestID = data_dict['RequestID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.OptSelfCloseFlag = chr(data_dict['OptSelfCloseFlag'])
            self.OptionSelfCloseLocalID = data_dict['OptionSelfCloseLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve1 = data_dict['reserve1']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OptionSelfCloseSysID = data_dict['OptionSelfCloseSysID']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.CancelTime = data_dict['CancelTime']
            self.ExecResult = chr(data_dict['ExecResult'])
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.BranchID = data_dict['BranchID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.Volume = 0
            self.RequestID = 0
            self.BusinessUnit = ''
            self.HedgeFlag = ''
            self.OptSelfCloseFlag = ''
            self.OptionSelfCloseLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve1 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OptionSelfCloseSysID = ''
            self.InsertDate = ''
            self.InsertTime = ''
            self.CancelTime = ''
            self.ExecResult = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.BranchID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryOptionSelfCloseActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''

class CThostFtdcExchangeOptionSelfCloseActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.OptionSelfCloseSysID = data_dict['OptionSelfCloseSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OptionSelfCloseLocalID = data_dict['OptionSelfCloseLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.BranchID = data_dict['BranchID']
            self.reserve1 = data_dict['reserve1']
            self.MacAddress = data_dict['MacAddress']
            self.reserve2 = data_dict['reserve2']
            self.OptSelfCloseFlag = chr(data_dict['OptSelfCloseFlag'])
            self.IPAddress = data_dict['IPAddress']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ExchangeID = ''
            self.OptionSelfCloseSysID = ''
            self.ActionFlag = ''
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OptionSelfCloseLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.BranchID = ''
            self.reserve1 = ''
            self.MacAddress = ''
            self.reserve2 = ''
            self.OptSelfCloseFlag = ''
            self.IPAddress = ''
            self.ExchangeInstID = ''

class CThostFtdcSyncDelaySwapField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.DelaySwapSeqNo = data_dict['DelaySwapSeqNo']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.FromCurrencyID = data_dict['FromCurrencyID']
            self.FromAmount = data_dict['FromAmount']
            self.FromFrozenSwap = data_dict['FromFrozenSwap']
            self.FromRemainSwap = data_dict['FromRemainSwap']
            self.ToCurrencyID = data_dict['ToCurrencyID']
            self.ToAmount = data_dict['ToAmount']
            self.IsManualSwap = data_dict['IsManualSwap']
            self.IsAllRemainSetZero = data_dict['IsAllRemainSetZero']
        else:
            self.DelaySwapSeqNo = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.FromCurrencyID = ''
            self.FromAmount = 0.0
            self.FromFrozenSwap = 0.0
            self.FromRemainSwap = 0.0
            self.ToCurrencyID = ''
            self.ToAmount = 0.0
            self.IsManualSwap = 0
            self.IsAllRemainSetZero = 0

class CThostFtdcQrySyncDelaySwapField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.DelaySwapSeqNo = data_dict['DelaySwapSeqNo']
        else:
            self.BrokerID = ''
            self.DelaySwapSeqNo = ''

class CThostFtdcInvestUnitField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InvestorUnitName = data_dict['InvestorUnitName']
            self.InvestorGroupID = data_dict['InvestorGroupID']
            self.CommModelID = data_dict['CommModelID']
            self.MarginModelID = data_dict['MarginModelID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.InvestUnitID = ''
            self.InvestorUnitName = ''
            self.InvestorGroupID = ''
            self.CommModelID = ''
            self.MarginModelID = ''
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcQryInvestUnitField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.InvestUnitID = ''

class CThostFtdcSecAgentCheckModeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InvestorID = data_dict['InvestorID']
            self.BrokerID = data_dict['BrokerID']
            self.CurrencyID = data_dict['CurrencyID']
            self.BrokerSecAgentID = data_dict['BrokerSecAgentID']
            self.CheckSelfAccount = data_dict['CheckSelfAccount']
        else:
            self.InvestorID = ''
            self.BrokerID = ''
            self.CurrencyID = ''
            self.BrokerSecAgentID = ''
            self.CheckSelfAccount = 0

class CThostFtdcSecAgentTradeInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.BrokerSecAgentID = data_dict['BrokerSecAgentID']
            self.InvestorID = data_dict['InvestorID']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.BrokerID = ''
            self.BrokerSecAgentID = ''
            self.InvestorID = ''
            self.LongCustomerName = ''

class CThostFtdcMarketDataField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve2 = data_dict['reserve2']
            self.LastPrice = data_dict['LastPrice']
            self.PreSettlementPrice = data_dict['PreSettlementPrice']
            self.PreClosePrice = data_dict['PreClosePrice']
            self.PreOpenInterest = data_dict['PreOpenInterest']
            self.OpenPrice = data_dict['OpenPrice']
            self.HighestPrice = data_dict['HighestPrice']
            self.LowestPrice = data_dict['LowestPrice']
            self.Volume = data_dict['Volume']
            self.Turnover = data_dict['Turnover']
            self.OpenInterest = data_dict['OpenInterest']
            self.ClosePrice = data_dict['ClosePrice']
            self.SettlementPrice = data_dict['SettlementPrice']
            self.UpperLimitPrice = data_dict['UpperLimitPrice']
            self.LowerLimitPrice = data_dict['LowerLimitPrice']
            self.PreDelta = data_dict['PreDelta']
            self.CurrDelta = data_dict['CurrDelta']
            self.UpdateTime = data_dict['UpdateTime']
            self.UpdateMillisec = data_dict['UpdateMillisec']
            self.ActionDay = data_dict['ActionDay']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.TradingDay = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.reserve2 = ''
            self.LastPrice = 0.0
            self.PreSettlementPrice = 0.0
            self.PreClosePrice = 0.0
            self.PreOpenInterest = 0.0
            self.OpenPrice = 0.0
            self.HighestPrice = 0.0
            self.LowestPrice = 0.0
            self.Volume = 0
            self.Turnover = 0.0
            self.OpenInterest = 0.0
            self.ClosePrice = 0.0
            self.SettlementPrice = 0.0
            self.UpperLimitPrice = 0.0
            self.LowerLimitPrice = 0.0
            self.PreDelta = 0.0
            self.CurrDelta = 0.0
            self.UpdateTime = ''
            self.UpdateMillisec = 0
            self.ActionDay = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''

class CThostFtdcMarketDataBaseField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.PreSettlementPrice = data_dict['PreSettlementPrice']
            self.PreClosePrice = data_dict['PreClosePrice']
            self.PreOpenInterest = data_dict['PreOpenInterest']
            self.PreDelta = data_dict['PreDelta']
        else:
            self.TradingDay = ''
            self.PreSettlementPrice = 0.0
            self.PreClosePrice = 0.0
            self.PreOpenInterest = 0.0
            self.PreDelta = 0.0

class CThostFtdcMarketDataStaticField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.OpenPrice = data_dict['OpenPrice']
            self.HighestPrice = data_dict['HighestPrice']
            self.LowestPrice = data_dict['LowestPrice']
            self.ClosePrice = data_dict['ClosePrice']
            self.UpperLimitPrice = data_dict['UpperLimitPrice']
            self.LowerLimitPrice = data_dict['LowerLimitPrice']
            self.SettlementPrice = data_dict['SettlementPrice']
            self.CurrDelta = data_dict['CurrDelta']
        else:
            self.OpenPrice = 0.0
            self.HighestPrice = 0.0
            self.LowestPrice = 0.0
            self.ClosePrice = 0.0
            self.UpperLimitPrice = 0.0
            self.LowerLimitPrice = 0.0
            self.SettlementPrice = 0.0
            self.CurrDelta = 0.0

class CThostFtdcMarketDataLastMatchField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.LastPrice = data_dict['LastPrice']
            self.Volume = data_dict['Volume']
            self.Turnover = data_dict['Turnover']
            self.OpenInterest = data_dict['OpenInterest']
        else:
            self.LastPrice = 0.0
            self.Volume = 0
            self.Turnover = 0.0
            self.OpenInterest = 0.0

class CThostFtdcMarketDataBestPriceField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BidPrice1 = data_dict['BidPrice1']
            self.BidVolume1 = data_dict['BidVolume1']
            self.AskPrice1 = data_dict['AskPrice1']
            self.AskVolume1 = data_dict['AskVolume1']
        else:
            self.BidPrice1 = 0.0
            self.BidVolume1 = 0
            self.AskPrice1 = 0.0
            self.AskVolume1 = 0

class CThostFtdcMarketDataBid23Field:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BidPrice2 = data_dict['BidPrice2']
            self.BidVolume2 = data_dict['BidVolume2']
            self.BidPrice3 = data_dict['BidPrice3']
            self.BidVolume3 = data_dict['BidVolume3']
        else:
            self.BidPrice2 = 0.0
            self.BidVolume2 = 0
            self.BidPrice3 = 0.0
            self.BidVolume3 = 0

class CThostFtdcMarketDataAsk23Field:
    def __init__(self, data_dict=None):
        if data_dict:
            self.AskPrice2 = data_dict['AskPrice2']
            self.AskVolume2 = data_dict['AskVolume2']
            self.AskPrice3 = data_dict['AskPrice3']
            self.AskVolume3 = data_dict['AskVolume3']
        else:
            self.AskPrice2 = 0.0
            self.AskVolume2 = 0
            self.AskPrice3 = 0.0
            self.AskVolume3 = 0

class CThostFtdcMarketDataBid45Field:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BidPrice4 = data_dict['BidPrice4']
            self.BidVolume4 = data_dict['BidVolume4']
            self.BidPrice5 = data_dict['BidPrice5']
            self.BidVolume5 = data_dict['BidVolume5']
        else:
            self.BidPrice4 = 0.0
            self.BidVolume4 = 0
            self.BidPrice5 = 0.0
            self.BidVolume5 = 0

class CThostFtdcMarketDataAsk45Field:
    def __init__(self, data_dict=None):
        if data_dict:
            self.AskPrice4 = data_dict['AskPrice4']
            self.AskVolume4 = data_dict['AskVolume4']
            self.AskPrice5 = data_dict['AskPrice5']
            self.AskVolume5 = data_dict['AskVolume5']
        else:
            self.AskPrice4 = 0.0
            self.AskVolume4 = 0
            self.AskPrice5 = 0.0
            self.AskVolume5 = 0

class CThostFtdcMarketDataUpdateTimeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.UpdateTime = data_dict['UpdateTime']
            self.UpdateMillisec = data_dict['UpdateMillisec']
            self.ActionDay = data_dict['ActionDay']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.UpdateTime = ''
            self.UpdateMillisec = 0
            self.ActionDay = ''
            self.InstrumentID = ''

class CThostFtdcMarketDataExchangeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.ExchangeID = ''

class CThostFtdcSpecificInstrumentField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcInstrumentStatusField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve1 = data_dict['reserve1']
            self.SettlementGroupID = data_dict['SettlementGroupID']
            self.reserve2 = data_dict['reserve2']
            self.InstrumentStatus = chr(data_dict['InstrumentStatus'])
            self.TradingSegmentSN = data_dict['TradingSegmentSN']
            self.EnterTime = data_dict['EnterTime']
            self.EnterReason = chr(data_dict['EnterReason'])
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.ExchangeID = ''
            self.reserve1 = ''
            self.SettlementGroupID = ''
            self.reserve2 = ''
            self.InstrumentStatus = ''
            self.TradingSegmentSN = 0
            self.EnterTime = ''
            self.EnterReason = ''
            self.ExchangeInstID = ''
            self.InstrumentID = ''

class CThostFtdcQryInstrumentStatusField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeInstID = data_dict['ExchangeInstID']
        else:
            self.ExchangeID = ''
            self.reserve1 = ''
            self.ExchangeInstID = ''

class CThostFtdcInvestorAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcPositionProfitAlgorithmField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.Algorithm = chr(data_dict['Algorithm'])
            self.Memo = data_dict['Memo']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.Algorithm = ''
            self.Memo = ''
            self.CurrencyID = ''

class CThostFtdcDiscountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.InvestorID = data_dict['InvestorID']
            self.Discount = data_dict['Discount']
        else:
            self.BrokerID = ''
            self.InvestorRange = ''
            self.InvestorID = ''
            self.Discount = 0.0

class CThostFtdcQryTransferBankField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BankID = data_dict['BankID']
            self.BankBrchID = data_dict['BankBrchID']
        else:
            self.BankID = ''
            self.BankBrchID = ''

class CThostFtdcTransferBankField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BankID = data_dict['BankID']
            self.BankBrchID = data_dict['BankBrchID']
            self.BankName = data_dict['BankName']
            self.IsActive = data_dict['IsActive']
        else:
            self.BankID = ''
            self.BankBrchID = ''
            self.BankName = ''
            self.IsActive = 0

class CThostFtdcQryInvestorPositionDetailField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcInvestorPositionDetailField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.Direction = chr(data_dict['Direction'])
            self.OpenDate = data_dict['OpenDate']
            self.TradeID = data_dict['TradeID']
            self.Volume = data_dict['Volume']
            self.OpenPrice = data_dict['OpenPrice']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.TradeType = chr(data_dict['TradeType'])
            self.reserve2 = data_dict['reserve2']
            self.ExchangeID = data_dict['ExchangeID']
            self.CloseProfitByDate = data_dict['CloseProfitByDate']
            self.CloseProfitByTrade = data_dict['CloseProfitByTrade']
            self.PositionProfitByDate = data_dict['PositionProfitByDate']
            self.PositionProfitByTrade = data_dict['PositionProfitByTrade']
            self.Margin = data_dict['Margin']
            self.ExchMargin = data_dict['ExchMargin']
            self.MarginRateByMoney = data_dict['MarginRateByMoney']
            self.MarginRateByVolume = data_dict['MarginRateByVolume']
            self.LastSettlementPrice = data_dict['LastSettlementPrice']
            self.SettlementPrice = data_dict['SettlementPrice']
            self.CloseVolume = data_dict['CloseVolume']
            self.CloseAmount = data_dict['CloseAmount']
            self.TimeFirstVolume = data_dict['TimeFirstVolume']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.SpecPosiType = chr(data_dict['SpecPosiType'])
            self.InstrumentID = data_dict['InstrumentID']
            self.CombInstrumentID = data_dict['CombInstrumentID']
        else:
            self.reserve1 = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.HedgeFlag = ''
            self.Direction = ''
            self.OpenDate = ''
            self.TradeID = ''
            self.Volume = 0
            self.OpenPrice = 0.0
            self.TradingDay = ''
            self.SettlementID = 0
            self.TradeType = ''
            self.reserve2 = ''
            self.ExchangeID = ''
            self.CloseProfitByDate = 0.0
            self.CloseProfitByTrade = 0.0
            self.PositionProfitByDate = 0.0
            self.PositionProfitByTrade = 0.0
            self.Margin = 0.0
            self.ExchMargin = 0.0
            self.MarginRateByMoney = 0.0
            self.MarginRateByVolume = 0.0
            self.LastSettlementPrice = 0.0
            self.SettlementPrice = 0.0
            self.CloseVolume = 0
            self.CloseAmount = 0.0
            self.TimeFirstVolume = 0
            self.InvestUnitID = ''
            self.SpecPosiType = ''
            self.InstrumentID = ''
            self.CombInstrumentID = ''

class CThostFtdcTradingAccountPasswordField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.Password = ''
            self.CurrencyID = ''

class CThostFtdcMDTraderOfferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.TraderID = data_dict['TraderID']
            self.ParticipantID = data_dict['ParticipantID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.TraderConnectStatus = chr(data_dict['TraderConnectStatus'])
            self.ConnectRequestDate = data_dict['ConnectRequestDate']
            self.ConnectRequestTime = data_dict['ConnectRequestTime']
            self.LastReportDate = data_dict['LastReportDate']
            self.LastReportTime = data_dict['LastReportTime']
            self.ConnectDate = data_dict['ConnectDate']
            self.ConnectTime = data_dict['ConnectTime']
            self.StartDate = data_dict['StartDate']
            self.StartTime = data_dict['StartTime']
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.MaxTradeID = data_dict['MaxTradeID']
            self.MaxOrderMessageReference = data_dict['MaxOrderMessageReference']
        else:
            self.ExchangeID = ''
            self.TraderID = ''
            self.ParticipantID = ''
            self.Password = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.TraderConnectStatus = ''
            self.ConnectRequestDate = ''
            self.ConnectRequestTime = ''
            self.LastReportDate = ''
            self.LastReportTime = ''
            self.ConnectDate = ''
            self.ConnectTime = ''
            self.StartDate = ''
            self.StartTime = ''
            self.TradingDay = ''
            self.BrokerID = ''
            self.MaxTradeID = ''
            self.MaxOrderMessageReference = ''

class CThostFtdcQryMDTraderOfferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.TraderID = data_dict['TraderID']
        else:
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.TraderID = ''

class CThostFtdcQryNoticeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
        else:
            self.BrokerID = ''

class CThostFtdcNoticeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.Content = data_dict['Content']
            self.SequenceLabel = data_dict['SequenceLabel']
        else:
            self.BrokerID = ''
            self.Content = ''
            self.SequenceLabel = ''

class CThostFtdcUserRightField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserRightType = chr(data_dict['UserRightType'])
            self.IsForbidden = data_dict['IsForbidden']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserRightType = ''
            self.IsForbidden = 0

class CThostFtdcQrySettlementInfoConfirmField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcLoadSettlementInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
        else:
            self.BrokerID = ''

class CThostFtdcBrokerWithdrawAlgorithmField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.WithdrawAlgorithm = chr(data_dict['WithdrawAlgorithm'])
            self.UsingRatio = data_dict['UsingRatio']
            self.IncludeCloseProfit = chr(data_dict['IncludeCloseProfit'])
            self.AllWithoutTrade = chr(data_dict['AllWithoutTrade'])
            self.AvailIncludeCloseProfit = chr(data_dict['AvailIncludeCloseProfit'])
            self.IsBrokerUserEvent = data_dict['IsBrokerUserEvent']
            self.CurrencyID = data_dict['CurrencyID']
            self.FundMortgageRatio = data_dict['FundMortgageRatio']
            self.BalanceAlgorithm = chr(data_dict['BalanceAlgorithm'])
        else:
            self.BrokerID = ''
            self.WithdrawAlgorithm = ''
            self.UsingRatio = 0.0
            self.IncludeCloseProfit = ''
            self.AllWithoutTrade = ''
            self.AvailIncludeCloseProfit = ''
            self.IsBrokerUserEvent = 0
            self.CurrencyID = ''
            self.FundMortgageRatio = 0.0
            self.BalanceAlgorithm = ''

class CThostFtdcTradingAccountPasswordUpdateV1Field:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OldPassword = data_dict['OldPassword']
            self.NewPassword = data_dict['NewPassword']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OldPassword = ''
            self.NewPassword = ''

class CThostFtdcTradingAccountPasswordUpdateField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.OldPassword = data_dict['OldPassword']
            self.NewPassword = data_dict['NewPassword']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.OldPassword = ''
            self.NewPassword = ''
            self.CurrencyID = ''

class CThostFtdcQryCombinationLegField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.LegID = data_dict['LegID']
            self.reserve2 = data_dict['reserve2']
            self.CombInstrumentID = data_dict['CombInstrumentID']
            self.LegInstrumentID = data_dict['LegInstrumentID']
        else:
            self.reserve1 = ''
            self.LegID = 0
            self.reserve2 = ''
            self.CombInstrumentID = ''
            self.LegInstrumentID = ''

class CThostFtdcQrySyncStatusField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
        else:
            self.TradingDay = ''

class CThostFtdcCombinationLegField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.LegID = data_dict['LegID']
            self.reserve2 = data_dict['reserve2']
            self.Direction = chr(data_dict['Direction'])
            self.LegMultiple = data_dict['LegMultiple']
            self.ImplyLevel = data_dict['ImplyLevel']
            self.CombInstrumentID = data_dict['CombInstrumentID']
            self.LegInstrumentID = data_dict['LegInstrumentID']
        else:
            self.reserve1 = ''
            self.LegID = 0
            self.reserve2 = ''
            self.Direction = ''
            self.LegMultiple = 0
            self.ImplyLevel = 0
            self.CombInstrumentID = ''
            self.LegInstrumentID = ''

class CThostFtdcSyncStatusField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.DataSyncStatus = chr(data_dict['DataSyncStatus'])
        else:
            self.TradingDay = ''
            self.DataSyncStatus = ''

class CThostFtdcQryLinkManField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcLinkManField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.PersonType = chr(data_dict['PersonType'])
            self.IdentifiedCardType = chr(data_dict['IdentifiedCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.PersonName = data_dict['PersonName']
            self.Telephone = data_dict['Telephone']
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Priority = data_dict['Priority']
            self.UOAZipCode = data_dict['UOAZipCode']
            self.PersonFullName = data_dict['PersonFullName']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.PersonType = ''
            self.IdentifiedCardType = ''
            self.IdentifiedCardNo = ''
            self.PersonName = ''
            self.Telephone = ''
            self.Address = ''
            self.ZipCode = ''
            self.Priority = 0
            self.UOAZipCode = ''
            self.PersonFullName = ''

class CThostFtdcQryBrokerUserEventField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserEventType = chr(data_dict['UserEventType'])
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserEventType = ''

class CThostFtdcBrokerUserEventField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.UserEventType = chr(data_dict['UserEventType'])
            self.EventSequenceNo = data_dict['EventSequenceNo']
            self.EventDate = data_dict['EventDate']
            self.EventTime = data_dict['EventTime']
            self.UserEventInfo = data_dict['UserEventInfo']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.UserEventType = ''
            self.EventSequenceNo = 0
            self.EventDate = ''
            self.EventTime = ''
            self.UserEventInfo = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcQryContractBankField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.BankID = data_dict['BankID']
            self.BankBrchID = data_dict['BankBrchID']
        else:
            self.BrokerID = ''
            self.BankID = ''
            self.BankBrchID = ''

class CThostFtdcContractBankField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.BankID = data_dict['BankID']
            self.BankBrchID = data_dict['BankBrchID']
            self.BankName = data_dict['BankName']
        else:
            self.BrokerID = ''
            self.BankID = ''
            self.BankBrchID = ''
            self.BankName = ''

class CThostFtdcInvestorPositionCombineDetailField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.OpenDate = data_dict['OpenDate']
            self.ExchangeID = data_dict['ExchangeID']
            self.SettlementID = data_dict['SettlementID']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ComTradeID = data_dict['ComTradeID']
            self.TradeID = data_dict['TradeID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.Direction = chr(data_dict['Direction'])
            self.TotalAmt = data_dict['TotalAmt']
            self.Margin = data_dict['Margin']
            self.ExchMargin = data_dict['ExchMargin']
            self.MarginRateByMoney = data_dict['MarginRateByMoney']
            self.MarginRateByVolume = data_dict['MarginRateByVolume']
            self.LegID = data_dict['LegID']
            self.LegMultiple = data_dict['LegMultiple']
            self.reserve2 = data_dict['reserve2']
            self.TradeGroupID = data_dict['TradeGroupID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
            self.CombInstrumentID = data_dict['CombInstrumentID']
        else:
            self.TradingDay = ''
            self.OpenDate = ''
            self.ExchangeID = ''
            self.SettlementID = 0
            self.BrokerID = ''
            self.InvestorID = ''
            self.ComTradeID = ''
            self.TradeID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.Direction = ''
            self.TotalAmt = 0
            self.Margin = 0.0
            self.ExchMargin = 0.0
            self.MarginRateByMoney = 0.0
            self.MarginRateByVolume = 0.0
            self.LegID = 0
            self.LegMultiple = 0
            self.reserve2 = ''
            self.TradeGroupID = 0
            self.InvestUnitID = ''
            self.InstrumentID = ''
            self.CombInstrumentID = ''

class CThostFtdcParkedOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OrderRef = data_dict['OrderRef']
            self.UserID = data_dict['UserID']
            self.OrderPriceType = chr(data_dict['OrderPriceType'])
            self.Direction = chr(data_dict['Direction'])
            self.CombOffsetFlag = data_dict['CombOffsetFlag']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeTotalOriginal = data_dict['VolumeTotalOriginal']
            self.TimeCondition = chr(data_dict['TimeCondition'])
            self.GTDDate = data_dict['GTDDate']
            self.VolumeCondition = chr(data_dict['VolumeCondition'])
            self.MinVolume = data_dict['MinVolume']
            self.ContingentCondition = chr(data_dict['ContingentCondition'])
            self.StopPrice = data_dict['StopPrice']
            self.ForceCloseReason = chr(data_dict['ForceCloseReason'])
            self.IsAutoSuspend = data_dict['IsAutoSuspend']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.RequestID = data_dict['RequestID']
            self.UserForceClose = data_dict['UserForceClose']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParkedOrderID = data_dict['ParkedOrderID']
            self.UserType = chr(data_dict['UserType'])
            self.Status = chr(data_dict['Status'])
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.IsSwapOrder = data_dict['IsSwapOrder']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.ClientID = data_dict['ClientID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OrderRef = ''
            self.UserID = ''
            self.OrderPriceType = ''
            self.Direction = ''
            self.CombOffsetFlag = ''
            self.CombHedgeFlag = ''
            self.LimitPrice = 0.0
            self.VolumeTotalOriginal = 0
            self.TimeCondition = ''
            self.GTDDate = ''
            self.VolumeCondition = ''
            self.MinVolume = 0
            self.ContingentCondition = ''
            self.StopPrice = 0.0
            self.ForceCloseReason = ''
            self.IsAutoSuspend = 0
            self.BusinessUnit = ''
            self.RequestID = 0
            self.UserForceClose = 0
            self.ExchangeID = ''
            self.ParkedOrderID = ''
            self.UserType = ''
            self.Status = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.IsSwapOrder = 0
            self.AccountID = ''
            self.CurrencyID = ''
            self.ClientID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcParkedOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OrderActionRef = data_dict['OrderActionRef']
            self.OrderRef = data_dict['OrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeChange = data_dict['VolumeChange']
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.ParkedOrderActionID = data_dict['ParkedOrderActionID']
            self.UserType = chr(data_dict['UserType'])
            self.Status = chr(data_dict['Status'])
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OrderActionRef = 0
            self.OrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.ActionFlag = ''
            self.LimitPrice = 0.0
            self.VolumeChange = 0
            self.UserID = ''
            self.reserve1 = ''
            self.ParkedOrderActionID = ''
            self.UserType = ''
            self.Status = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryParkedOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryParkedOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcRemoveParkedOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ParkedOrderID = data_dict['ParkedOrderID']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ParkedOrderID = ''
            self.InvestUnitID = ''

class CThostFtdcRemoveParkedOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ParkedOrderActionID = data_dict['ParkedOrderActionID']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ParkedOrderActionID = ''
            self.InvestUnitID = ''

class CThostFtdcInvestorWithdrawAlgorithmField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.InvestorID = data_dict['InvestorID']
            self.UsingRatio = data_dict['UsingRatio']
            self.CurrencyID = data_dict['CurrencyID']
            self.FundMortgageRatio = data_dict['FundMortgageRatio']
        else:
            self.BrokerID = ''
            self.InvestorRange = ''
            self.InvestorID = ''
            self.UsingRatio = 0.0
            self.CurrencyID = ''
            self.FundMortgageRatio = 0.0

class CThostFtdcQryInvestorPositionCombineDetailField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.CombInstrumentID = data_dict['CombInstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.CombInstrumentID = ''

class CThostFtdcMarketDataAveragePriceField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.AveragePrice = data_dict['AveragePrice']
        else:
            self.AveragePrice = 0.0

class CThostFtdcVerifyInvestorPasswordField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.Password = data_dict['Password']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.Password = ''

class CThostFtdcUserIPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.IPAddress = data_dict['IPAddress']
            self.IPMask = data_dict['IPMask']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.reserve1 = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.IPAddress = ''
            self.IPMask = ''

class CThostFtdcTradingNoticeInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.SendTime = data_dict['SendTime']
            self.FieldContent = data_dict['FieldContent']
            self.SequenceSeries = data_dict['SequenceSeries']
            self.SequenceNo = data_dict['SequenceNo']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.SendTime = ''
            self.FieldContent = ''
            self.SequenceSeries = 0
            self.SequenceNo = 0
            self.InvestUnitID = ''

class CThostFtdcTradingNoticeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.InvestorID = data_dict['InvestorID']
            self.SequenceSeries = data_dict['SequenceSeries']
            self.UserID = data_dict['UserID']
            self.SendTime = data_dict['SendTime']
            self.SequenceNo = data_dict['SequenceNo']
            self.FieldContent = data_dict['FieldContent']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorRange = ''
            self.InvestorID = ''
            self.SequenceSeries = 0
            self.UserID = ''
            self.SendTime = ''
            self.SequenceNo = 0
            self.FieldContent = ''
            self.InvestUnitID = ''

class CThostFtdcQryTradingNoticeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.InvestUnitID = ''

class CThostFtdcQryErrOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcErrOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OrderRef = data_dict['OrderRef']
            self.UserID = data_dict['UserID']
            self.OrderPriceType = chr(data_dict['OrderPriceType'])
            self.Direction = chr(data_dict['Direction'])
            self.CombOffsetFlag = data_dict['CombOffsetFlag']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeTotalOriginal = data_dict['VolumeTotalOriginal']
            self.TimeCondition = chr(data_dict['TimeCondition'])
            self.GTDDate = data_dict['GTDDate']
            self.VolumeCondition = chr(data_dict['VolumeCondition'])
            self.MinVolume = data_dict['MinVolume']
            self.ContingentCondition = chr(data_dict['ContingentCondition'])
            self.StopPrice = data_dict['StopPrice']
            self.ForceCloseReason = chr(data_dict['ForceCloseReason'])
            self.IsAutoSuspend = data_dict['IsAutoSuspend']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.RequestID = data_dict['RequestID']
            self.UserForceClose = data_dict['UserForceClose']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.IsSwapOrder = data_dict['IsSwapOrder']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OrderRef = ''
            self.UserID = ''
            self.OrderPriceType = ''
            self.Direction = ''
            self.CombOffsetFlag = ''
            self.CombHedgeFlag = ''
            self.LimitPrice = 0.0
            self.VolumeTotalOriginal = 0
            self.TimeCondition = ''
            self.GTDDate = ''
            self.VolumeCondition = ''
            self.MinVolume = 0
            self.ContingentCondition = ''
            self.StopPrice = 0.0
            self.ForceCloseReason = ''
            self.IsAutoSuspend = 0
            self.BusinessUnit = ''
            self.RequestID = 0
            self.UserForceClose = 0
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.IsSwapOrder = 0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcErrorConditionalOrderField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.OrderRef = data_dict['OrderRef']
            self.UserID = data_dict['UserID']
            self.OrderPriceType = chr(data_dict['OrderPriceType'])
            self.Direction = chr(data_dict['Direction'])
            self.CombOffsetFlag = data_dict['CombOffsetFlag']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeTotalOriginal = data_dict['VolumeTotalOriginal']
            self.TimeCondition = chr(data_dict['TimeCondition'])
            self.GTDDate = data_dict['GTDDate']
            self.VolumeCondition = chr(data_dict['VolumeCondition'])
            self.MinVolume = data_dict['MinVolume']
            self.ContingentCondition = chr(data_dict['ContingentCondition'])
            self.StopPrice = data_dict['StopPrice']
            self.ForceCloseReason = chr(data_dict['ForceCloseReason'])
            self.IsAutoSuspend = data_dict['IsAutoSuspend']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.RequestID = data_dict['RequestID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.reserve2 = data_dict['reserve2']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderSubmitStatus = chr(data_dict['OrderSubmitStatus'])
            self.NotifySequence = data_dict['NotifySequence']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.OrderSysID = data_dict['OrderSysID']
            self.OrderSource = chr(data_dict['OrderSource'])
            self.OrderStatus = chr(data_dict['OrderStatus'])
            self.OrderType = chr(data_dict['OrderType'])
            self.VolumeTraded = data_dict['VolumeTraded']
            self.VolumeTotal = data_dict['VolumeTotal']
            self.InsertDate = data_dict['InsertDate']
            self.InsertTime = data_dict['InsertTime']
            self.ActiveTime = data_dict['ActiveTime']
            self.SuspendTime = data_dict['SuspendTime']
            self.UpdateTime = data_dict['UpdateTime']
            self.CancelTime = data_dict['CancelTime']
            self.ActiveTraderID = data_dict['ActiveTraderID']
            self.ClearingPartID = data_dict['ClearingPartID']
            self.SequenceNo = data_dict['SequenceNo']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.StatusMsg = data_dict['StatusMsg']
            self.UserForceClose = data_dict['UserForceClose']
            self.ActiveUserID = data_dict['ActiveUserID']
            self.BrokerOrderSeq = data_dict['BrokerOrderSeq']
            self.RelativeOrderSysID = data_dict['RelativeOrderSysID']
            self.ZCETotalTradedVolume = data_dict['ZCETotalTradedVolume']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.IsSwapOrder = data_dict['IsSwapOrder']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.reserve3 = data_dict['reserve3']
            self.MacAddress = data_dict['MacAddress']
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.OrderRef = ''
            self.UserID = ''
            self.OrderPriceType = ''
            self.Direction = ''
            self.CombOffsetFlag = ''
            self.CombHedgeFlag = ''
            self.LimitPrice = 0.0
            self.VolumeTotalOriginal = 0
            self.TimeCondition = ''
            self.GTDDate = ''
            self.VolumeCondition = ''
            self.MinVolume = 0
            self.ContingentCondition = ''
            self.StopPrice = 0.0
            self.ForceCloseReason = ''
            self.IsAutoSuspend = 0
            self.BusinessUnit = ''
            self.RequestID = 0
            self.OrderLocalID = ''
            self.ExchangeID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.reserve2 = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderSubmitStatus = ''
            self.NotifySequence = 0
            self.TradingDay = ''
            self.SettlementID = 0
            self.OrderSysID = ''
            self.OrderSource = ''
            self.OrderStatus = ''
            self.OrderType = ''
            self.VolumeTraded = 0
            self.VolumeTotal = 0
            self.InsertDate = ''
            self.InsertTime = ''
            self.ActiveTime = ''
            self.SuspendTime = ''
            self.UpdateTime = ''
            self.CancelTime = ''
            self.ActiveTraderID = ''
            self.ClearingPartID = ''
            self.SequenceNo = 0
            self.FrontID = 0
            self.SessionID = 0
            self.UserProductInfo = ''
            self.StatusMsg = ''
            self.UserForceClose = 0
            self.ActiveUserID = ''
            self.BrokerOrderSeq = 0
            self.RelativeOrderSysID = ''
            self.ZCETotalTradedVolume = 0
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.IsSwapOrder = 0
            self.BranchID = ''
            self.InvestUnitID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.reserve3 = ''
            self.MacAddress = ''
            self.InstrumentID = ''
            self.ExchangeInstID = ''
            self.IPAddress = ''

class CThostFtdcQryErrOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcErrOrderActionField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.OrderActionRef = data_dict['OrderActionRef']
            self.OrderRef = data_dict['OrderRef']
            self.RequestID = data_dict['RequestID']
            self.FrontID = data_dict['FrontID']
            self.SessionID = data_dict['SessionID']
            self.ExchangeID = data_dict['ExchangeID']
            self.OrderSysID = data_dict['OrderSysID']
            self.ActionFlag = chr(data_dict['ActionFlag'])
            self.LimitPrice = data_dict['LimitPrice']
            self.VolumeChange = data_dict['VolumeChange']
            self.ActionDate = data_dict['ActionDate']
            self.ActionTime = data_dict['ActionTime']
            self.TraderID = data_dict['TraderID']
            self.InstallID = data_dict['InstallID']
            self.OrderLocalID = data_dict['OrderLocalID']
            self.ActionLocalID = data_dict['ActionLocalID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ClientID = data_dict['ClientID']
            self.BusinessUnit = data_dict['BusinessUnit']
            self.OrderActionStatus = chr(data_dict['OrderActionStatus'])
            self.UserID = data_dict['UserID']
            self.StatusMsg = data_dict['StatusMsg']
            self.reserve1 = data_dict['reserve1']
            self.BranchID = data_dict['BranchID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.reserve2 = data_dict['reserve2']
            self.MacAddress = data_dict['MacAddress']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.InstrumentID = data_dict['InstrumentID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.OrderActionRef = 0
            self.OrderRef = ''
            self.RequestID = 0
            self.FrontID = 0
            self.SessionID = 0
            self.ExchangeID = ''
            self.OrderSysID = ''
            self.ActionFlag = ''
            self.LimitPrice = 0.0
            self.VolumeChange = 0
            self.ActionDate = ''
            self.ActionTime = ''
            self.TraderID = ''
            self.InstallID = 0
            self.OrderLocalID = ''
            self.ActionLocalID = ''
            self.ParticipantID = ''
            self.ClientID = ''
            self.BusinessUnit = ''
            self.OrderActionStatus = ''
            self.UserID = ''
            self.StatusMsg = ''
            self.reserve1 = ''
            self.BranchID = ''
            self.InvestUnitID = ''
            self.reserve2 = ''
            self.MacAddress = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.InstrumentID = ''
            self.IPAddress = ''

class CThostFtdcQryExchangeSequenceField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.ExchangeID = ''

class CThostFtdcExchangeSequenceField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.SequenceNo = data_dict['SequenceNo']
            self.MarketStatus = chr(data_dict['MarketStatus'])
        else:
            self.ExchangeID = ''
            self.SequenceNo = 0
            self.MarketStatus = ''

class CThostFtdcQryMaxOrderVolumeWithPriceField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.Direction = chr(data_dict['Direction'])
            self.OffsetFlag = chr(data_dict['OffsetFlag'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.MaxVolume = data_dict['MaxVolume']
            self.Price = data_dict['Price']
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.Direction = ''
            self.OffsetFlag = ''
            self.HedgeFlag = ''
            self.MaxVolume = 0
            self.Price = 0.0
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryBrokerTradingParamsField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.CurrencyID = data_dict['CurrencyID']
            self.AccountID = data_dict['AccountID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.CurrencyID = ''
            self.AccountID = ''

class CThostFtdcBrokerTradingParamsField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.MarginPriceType = chr(data_dict['MarginPriceType'])
            self.Algorithm = chr(data_dict['Algorithm'])
            self.AvailIncludeCloseProfit = chr(data_dict['AvailIncludeCloseProfit'])
            self.CurrencyID = data_dict['CurrencyID']
            self.OptionRoyaltyPriceType = chr(data_dict['OptionRoyaltyPriceType'])
            self.AccountID = data_dict['AccountID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.MarginPriceType = ''
            self.Algorithm = ''
            self.AvailIncludeCloseProfit = ''
            self.CurrencyID = ''
            self.OptionRoyaltyPriceType = ''
            self.AccountID = ''

class CThostFtdcQryBrokerTradingAlgosField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.ExchangeID = ''
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcBrokerTradingAlgosField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve1 = data_dict['reserve1']
            self.HandlePositionAlgoID = chr(data_dict['HandlePositionAlgoID'])
            self.FindMarginRateAlgoID = chr(data_dict['FindMarginRateAlgoID'])
            self.HandleTradingAccountAlgoID = chr(data_dict['HandleTradingAccountAlgoID'])
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.ExchangeID = ''
            self.reserve1 = ''
            self.HandlePositionAlgoID = ''
            self.FindMarginRateAlgoID = ''
            self.HandleTradingAccountAlgoID = ''
            self.InstrumentID = ''

class CThostFtdcQueryBrokerDepositField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ExchangeID = data_dict['ExchangeID']
        else:
            self.BrokerID = ''
            self.ExchangeID = ''

class CThostFtdcBrokerDepositField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.ParticipantID = data_dict['ParticipantID']
            self.ExchangeID = data_dict['ExchangeID']
            self.PreBalance = data_dict['PreBalance']
            self.CurrMargin = data_dict['CurrMargin']
            self.CloseProfit = data_dict['CloseProfit']
            self.Balance = data_dict['Balance']
            self.Deposit = data_dict['Deposit']
            self.Withdraw = data_dict['Withdraw']
            self.Available = data_dict['Available']
            self.Reserve = data_dict['Reserve']
            self.FrozenMargin = data_dict['FrozenMargin']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.ParticipantID = ''
            self.ExchangeID = ''
            self.PreBalance = 0.0
            self.CurrMargin = 0.0
            self.CloseProfit = 0.0
            self.Balance = 0.0
            self.Deposit = 0.0
            self.Withdraw = 0.0
            self.Available = 0.0
            self.Reserve = 0.0
            self.FrozenMargin = 0.0

class CThostFtdcQryCFMMCBrokerKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
        else:
            self.BrokerID = ''

class CThostFtdcCFMMCBrokerKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ParticipantID = data_dict['ParticipantID']
            self.CreateDate = data_dict['CreateDate']
            self.CreateTime = data_dict['CreateTime']
            self.KeyID = data_dict['KeyID']
            self.CurrentKey = data_dict['CurrentKey']
            self.KeyKind = chr(data_dict['KeyKind'])
        else:
            self.BrokerID = ''
            self.ParticipantID = ''
            self.CreateDate = ''
            self.CreateTime = ''
            self.KeyID = 0
            self.CurrentKey = ''
            self.KeyKind = ''

class CThostFtdcCFMMCTradingAccountKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ParticipantID = data_dict['ParticipantID']
            self.AccountID = data_dict['AccountID']
            self.KeyID = data_dict['KeyID']
            self.CurrentKey = data_dict['CurrentKey']
        else:
            self.BrokerID = ''
            self.ParticipantID = ''
            self.AccountID = ''
            self.KeyID = 0
            self.CurrentKey = ''

class CThostFtdcQryCFMMCTradingAccountKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcBrokerUserOTPParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.OTPVendorsID = data_dict['OTPVendorsID']
            self.SerialNumber = data_dict['SerialNumber']
            self.AuthKey = data_dict['AuthKey']
            self.LastDrift = data_dict['LastDrift']
            self.LastSuccess = data_dict['LastSuccess']
            self.OTPType = chr(data_dict['OTPType'])
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.OTPVendorsID = ''
            self.SerialNumber = ''
            self.AuthKey = ''
            self.LastDrift = 0
            self.LastSuccess = 0
            self.OTPType = ''

class CThostFtdcManualSyncBrokerUserOTPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.OTPType = chr(data_dict['OTPType'])
            self.FirstOTP = data_dict['FirstOTP']
            self.SecondOTP = data_dict['SecondOTP']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.OTPType = ''
            self.FirstOTP = ''
            self.SecondOTP = ''

class CThostFtdcCommRateModelField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.CommModelID = data_dict['CommModelID']
            self.CommModelName = data_dict['CommModelName']
        else:
            self.BrokerID = ''
            self.CommModelID = ''
            self.CommModelName = ''

class CThostFtdcQryCommRateModelField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.CommModelID = data_dict['CommModelID']
        else:
            self.BrokerID = ''
            self.CommModelID = ''

class CThostFtdcMarginModelField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.MarginModelID = data_dict['MarginModelID']
            self.MarginModelName = data_dict['MarginModelName']
        else:
            self.BrokerID = ''
            self.MarginModelID = ''
            self.MarginModelName = ''

class CThostFtdcQryMarginModelField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.MarginModelID = data_dict['MarginModelID']
        else:
            self.BrokerID = ''
            self.MarginModelID = ''

class CThostFtdcEWarrantOffsetField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve1 = data_dict['reserve1']
            self.Direction = chr(data_dict['Direction'])
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.Volume = data_dict['Volume']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''
            self.reserve1 = ''
            self.Direction = ''
            self.HedgeFlag = ''
            self.Volume = 0
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryEWarrantOffsetField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve1 = data_dict['reserve1']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.ExchangeID = ''
            self.reserve1 = ''
            self.InvestUnitID = ''
            self.InstrumentID = ''

class CThostFtdcQryInvestorProductGroupMarginField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.reserve1 = data_dict['reserve1']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.ProductGroupID = data_dict['ProductGroupID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.reserve1 = ''
            self.HedgeFlag = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.ProductGroupID = ''

class CThostFtdcInvestorProductGroupMarginField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.TradingDay = data_dict['TradingDay']
            self.SettlementID = data_dict['SettlementID']
            self.FrozenMargin = data_dict['FrozenMargin']
            self.LongFrozenMargin = data_dict['LongFrozenMargin']
            self.ShortFrozenMargin = data_dict['ShortFrozenMargin']
            self.UseMargin = data_dict['UseMargin']
            self.LongUseMargin = data_dict['LongUseMargin']
            self.ShortUseMargin = data_dict['ShortUseMargin']
            self.ExchMargin = data_dict['ExchMargin']
            self.LongExchMargin = data_dict['LongExchMargin']
            self.ShortExchMargin = data_dict['ShortExchMargin']
            self.CloseProfit = data_dict['CloseProfit']
            self.FrozenCommission = data_dict['FrozenCommission']
            self.Commission = data_dict['Commission']
            self.FrozenCash = data_dict['FrozenCash']
            self.CashIn = data_dict['CashIn']
            self.PositionProfit = data_dict['PositionProfit']
            self.OffsetAmount = data_dict['OffsetAmount']
            self.LongOffsetAmount = data_dict['LongOffsetAmount']
            self.ShortOffsetAmount = data_dict['ShortOffsetAmount']
            self.ExchOffsetAmount = data_dict['ExchOffsetAmount']
            self.LongExchOffsetAmount = data_dict['LongExchOffsetAmount']
            self.ShortExchOffsetAmount = data_dict['ShortExchOffsetAmount']
            self.HedgeFlag = chr(data_dict['HedgeFlag'])
            self.ExchangeID = data_dict['ExchangeID']
            self.InvestUnitID = data_dict['InvestUnitID']
            self.ProductGroupID = data_dict['ProductGroupID']
        else:
            self.reserve1 = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.TradingDay = ''
            self.SettlementID = 0
            self.FrozenMargin = 0.0
            self.LongFrozenMargin = 0.0
            self.ShortFrozenMargin = 0.0
            self.UseMargin = 0.0
            self.LongUseMargin = 0.0
            self.ShortUseMargin = 0.0
            self.ExchMargin = 0.0
            self.LongExchMargin = 0.0
            self.ShortExchMargin = 0.0
            self.CloseProfit = 0.0
            self.FrozenCommission = 0.0
            self.Commission = 0.0
            self.FrozenCash = 0.0
            self.CashIn = 0.0
            self.PositionProfit = 0.0
            self.OffsetAmount = 0.0
            self.LongOffsetAmount = 0.0
            self.ShortOffsetAmount = 0.0
            self.ExchOffsetAmount = 0.0
            self.LongExchOffsetAmount = 0.0
            self.ShortExchOffsetAmount = 0.0
            self.HedgeFlag = ''
            self.ExchangeID = ''
            self.InvestUnitID = ''
            self.ProductGroupID = ''

class CThostFtdcQueryCFMMCTradingAccountTokenField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.InvestUnitID = data_dict['InvestUnitID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''
            self.InvestUnitID = ''

class CThostFtdcCFMMCTradingAccountTokenField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.ParticipantID = data_dict['ParticipantID']
            self.AccountID = data_dict['AccountID']
            self.KeyID = data_dict['KeyID']
            self.Token = data_dict['Token']
        else:
            self.BrokerID = ''
            self.ParticipantID = ''
            self.AccountID = ''
            self.KeyID = 0
            self.Token = ''

class CThostFtdcQryProductGroupField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.ProductID = data_dict['ProductID']
        else:
            self.reserve1 = ''
            self.ExchangeID = ''
            self.ProductID = ''

class CThostFtdcProductGroupField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.ExchangeID = data_dict['ExchangeID']
            self.reserve2 = data_dict['reserve2']
            self.ProductID = data_dict['ProductID']
            self.ProductGroupID = data_dict['ProductGroupID']
        else:
            self.reserve1 = ''
            self.ExchangeID = ''
            self.reserve2 = ''
            self.ProductID = ''
            self.ProductGroupID = ''

class CThostFtdcBulletinField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.TradingDay = data_dict['TradingDay']
            self.BulletinID = data_dict['BulletinID']
            self.SequenceNo = data_dict['SequenceNo']
            self.NewsType = data_dict['NewsType']
            self.NewsUrgency = chr(data_dict['NewsUrgency'])
            self.SendTime = data_dict['SendTime']
            self.Abstract = data_dict['Abstract']
            self.ComeFrom = data_dict['ComeFrom']
            self.Content = data_dict['Content']
            self.URLLink = data_dict['URLLink']
            self.MarketID = data_dict['MarketID']
        else:
            self.ExchangeID = ''
            self.TradingDay = ''
            self.BulletinID = 0
            self.SequenceNo = 0
            self.NewsType = ''
            self.NewsUrgency = ''
            self.SendTime = ''
            self.Abstract = ''
            self.ComeFrom = ''
            self.Content = ''
            self.URLLink = ''
            self.MarketID = ''

class CThostFtdcQryBulletinField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.BulletinID = data_dict['BulletinID']
            self.SequenceNo = data_dict['SequenceNo']
            self.NewsType = data_dict['NewsType']
            self.NewsUrgency = chr(data_dict['NewsUrgency'])
        else:
            self.ExchangeID = ''
            self.BulletinID = 0
            self.SequenceNo = 0
            self.NewsType = ''
            self.NewsUrgency = ''

class CThostFtdcMulticastInstrumentField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TopicID = data_dict['TopicID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentNo = data_dict['InstrumentNo']
            self.CodePrice = data_dict['CodePrice']
            self.VolumeMultiple = data_dict['VolumeMultiple']
            self.PriceTick = data_dict['PriceTick']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.TopicID = 0
            self.reserve1 = ''
            self.InstrumentNo = 0
            self.CodePrice = 0.0
            self.VolumeMultiple = 0
            self.PriceTick = 0.0
            self.InstrumentID = ''

class CThostFtdcQryMulticastInstrumentField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TopicID = data_dict['TopicID']
            self.reserve1 = data_dict['reserve1']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.TopicID = 0
            self.reserve1 = ''
            self.InstrumentID = ''

class CThostFtdcAppIDAuthAssignField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AppID = data_dict['AppID']
            self.DRIdentityID = data_dict['DRIdentityID']
        else:
            self.BrokerID = ''
            self.AppID = ''
            self.DRIdentityID = 0

class CThostFtdcReqOpenAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.CashExchangeCode = chr(data_dict['CashExchangeCode'])
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.TID = data_dict['TID']
            self.UserID = data_dict['UserID']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.CashExchangeCode = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.TID = 0
            self.UserID = ''
            self.LongCustomerName = ''

class CThostFtdcReqCancelAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.CashExchangeCode = chr(data_dict['CashExchangeCode'])
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.TID = data_dict['TID']
            self.UserID = data_dict['UserID']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.CashExchangeCode = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.TID = 0
            self.UserID = ''
            self.LongCustomerName = ''

class CThostFtdcReqChangeAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.NewBankAccount = data_dict['NewBankAccount']
            self.NewBankPassWord = data_dict['NewBankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.TID = data_dict['TID']
            self.Digest = data_dict['Digest']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.NewBankAccount = ''
            self.NewBankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.BankAccType = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.BrokerIDByBank = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.TID = 0
            self.Digest = ''
            self.LongCustomerName = ''

class CThostFtdcReqTransferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.FutureSerial = data_dict['FutureSerial']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.FutureFetchAmount = data_dict['FutureFetchAmount']
            self.FeePayFlag = chr(data_dict['FeePayFlag'])
            self.CustFee = data_dict['CustFee']
            self.BrokerFee = data_dict['BrokerFee']
            self.Message = data_dict['Message']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.TransferStatus = chr(data_dict['TransferStatus'])
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.FutureSerial = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.FutureFetchAmount = 0.0
            self.FeePayFlag = ''
            self.CustFee = 0.0
            self.BrokerFee = 0.0
            self.Message = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.TransferStatus = ''
            self.LongCustomerName = ''

class CThostFtdcRspTransferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.FutureSerial = data_dict['FutureSerial']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.FutureFetchAmount = data_dict['FutureFetchAmount']
            self.FeePayFlag = chr(data_dict['FeePayFlag'])
            self.CustFee = data_dict['CustFee']
            self.BrokerFee = data_dict['BrokerFee']
            self.Message = data_dict['Message']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.TransferStatus = chr(data_dict['TransferStatus'])
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.FutureSerial = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.FutureFetchAmount = 0.0
            self.FeePayFlag = ''
            self.CustFee = 0.0
            self.BrokerFee = 0.0
            self.Message = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.TransferStatus = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.LongCustomerName = ''

class CThostFtdcReqRepealField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.RepealTimeInterval = data_dict['RepealTimeInterval']
            self.RepealedTimes = data_dict['RepealedTimes']
            self.BankRepealFlag = chr(data_dict['BankRepealFlag'])
            self.BrokerRepealFlag = chr(data_dict['BrokerRepealFlag'])
            self.PlateRepealSerial = data_dict['PlateRepealSerial']
            self.BankRepealSerial = data_dict['BankRepealSerial']
            self.FutureRepealSerial = data_dict['FutureRepealSerial']
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.FutureSerial = data_dict['FutureSerial']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.FutureFetchAmount = data_dict['FutureFetchAmount']
            self.FeePayFlag = chr(data_dict['FeePayFlag'])
            self.CustFee = data_dict['CustFee']
            self.BrokerFee = data_dict['BrokerFee']
            self.Message = data_dict['Message']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.TransferStatus = chr(data_dict['TransferStatus'])
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.RepealTimeInterval = 0
            self.RepealedTimes = 0
            self.BankRepealFlag = ''
            self.BrokerRepealFlag = ''
            self.PlateRepealSerial = 0
            self.BankRepealSerial = ''
            self.FutureRepealSerial = 0
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.FutureSerial = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.FutureFetchAmount = 0.0
            self.FeePayFlag = ''
            self.CustFee = 0.0
            self.BrokerFee = 0.0
            self.Message = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.TransferStatus = ''
            self.LongCustomerName = ''

class CThostFtdcRspRepealField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.RepealTimeInterval = data_dict['RepealTimeInterval']
            self.RepealedTimes = data_dict['RepealedTimes']
            self.BankRepealFlag = chr(data_dict['BankRepealFlag'])
            self.BrokerRepealFlag = chr(data_dict['BrokerRepealFlag'])
            self.PlateRepealSerial = data_dict['PlateRepealSerial']
            self.BankRepealSerial = data_dict['BankRepealSerial']
            self.FutureRepealSerial = data_dict['FutureRepealSerial']
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.FutureSerial = data_dict['FutureSerial']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.FutureFetchAmount = data_dict['FutureFetchAmount']
            self.FeePayFlag = chr(data_dict['FeePayFlag'])
            self.CustFee = data_dict['CustFee']
            self.BrokerFee = data_dict['BrokerFee']
            self.Message = data_dict['Message']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.TransferStatus = chr(data_dict['TransferStatus'])
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.RepealTimeInterval = 0
            self.RepealedTimes = 0
            self.BankRepealFlag = ''
            self.BrokerRepealFlag = ''
            self.PlateRepealSerial = 0
            self.BankRepealSerial = ''
            self.FutureRepealSerial = 0
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.FutureSerial = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.FutureFetchAmount = 0.0
            self.FeePayFlag = ''
            self.CustFee = 0.0
            self.BrokerFee = 0.0
            self.Message = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.TransferStatus = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.LongCustomerName = ''

class CThostFtdcReqQueryAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.FutureSerial = data_dict['FutureSerial']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.FutureSerial = 0
            self.InstallID = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.LongCustomerName = ''

class CThostFtdcRspQueryAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.FutureSerial = data_dict['FutureSerial']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.BankUseAmount = data_dict['BankUseAmount']
            self.BankFetchAmount = data_dict['BankFetchAmount']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.FutureSerial = 0
            self.InstallID = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.BankUseAmount = 0.0
            self.BankFetchAmount = 0.0
            self.LongCustomerName = ''

class CThostFtdcFutureSignIOField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Digest = data_dict['Digest']
            self.CurrencyID = data_dict['CurrencyID']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Digest = ''
            self.CurrencyID = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0

class CThostFtdcRspFutureSignInField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Digest = data_dict['Digest']
            self.CurrencyID = data_dict['CurrencyID']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.PinKey = data_dict['PinKey']
            self.MacKey = data_dict['MacKey']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Digest = ''
            self.CurrencyID = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.PinKey = ''
            self.MacKey = ''

class CThostFtdcReqFutureSignOutField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Digest = data_dict['Digest']
            self.CurrencyID = data_dict['CurrencyID']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Digest = ''
            self.CurrencyID = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0

class CThostFtdcRspFutureSignOutField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Digest = data_dict['Digest']
            self.CurrencyID = data_dict['CurrencyID']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Digest = ''
            self.CurrencyID = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcReqQueryTradeResultBySerialField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.Reference = data_dict['Reference']
            self.RefrenceIssureType = chr(data_dict['RefrenceIssureType'])
            self.RefrenceIssure = data_dict['RefrenceIssure']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.Digest = data_dict['Digest']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.Reference = 0
            self.RefrenceIssureType = ''
            self.RefrenceIssure = ''
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.Digest = ''
            self.LongCustomerName = ''

class CThostFtdcRspQueryTradeResultBySerialField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.Reference = data_dict['Reference']
            self.RefrenceIssureType = chr(data_dict['RefrenceIssureType'])
            self.RefrenceIssure = data_dict['RefrenceIssure']
            self.OriginReturnCode = data_dict['OriginReturnCode']
            self.OriginDescrInfoForReturnCode = data_dict['OriginDescrInfoForReturnCode']
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.Digest = data_dict['Digest']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.Reference = 0
            self.RefrenceIssureType = ''
            self.RefrenceIssure = ''
            self.OriginReturnCode = ''
            self.OriginDescrInfoForReturnCode = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.Digest = ''

class CThostFtdcReqDayEndFileReadyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.FileBusinessCode = chr(data_dict['FileBusinessCode'])
            self.Digest = data_dict['Digest']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.FileBusinessCode = ''
            self.Digest = ''

class CThostFtdcReturnResultField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ReturnCode = data_dict['ReturnCode']
            self.DescrInfoForReturnCode = data_dict['DescrInfoForReturnCode']
        else:
            self.ReturnCode = ''
            self.DescrInfoForReturnCode = ''

class CThostFtdcVerifyFuturePasswordField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.InstallID = data_dict['InstallID']
            self.TID = data_dict['TID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.AccountID = ''
            self.Password = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.InstallID = 0
            self.TID = 0
            self.CurrencyID = ''

class CThostFtdcVerifyCustInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.LongCustomerName = ''

class CThostFtdcVerifyFuturePasswordAndCustInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.CurrencyID = data_dict['CurrencyID']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.AccountID = ''
            self.Password = ''
            self.CurrencyID = ''
            self.LongCustomerName = ''

class CThostFtdcDepositResultInformField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.DepositSeqNo = data_dict['DepositSeqNo']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.Deposit = data_dict['Deposit']
            self.RequestID = data_dict['RequestID']
            self.ReturnCode = data_dict['ReturnCode']
            self.DescrInfoForReturnCode = data_dict['DescrInfoForReturnCode']
        else:
            self.DepositSeqNo = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.Deposit = 0.0
            self.RequestID = 0
            self.ReturnCode = ''
            self.DescrInfoForReturnCode = ''

class CThostFtdcReqSyncKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Message = data_dict['Message']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Message = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0

class CThostFtdcRspSyncKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Message = data_dict['Message']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Message = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcNotifyQueryAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.FutureSerial = data_dict['FutureSerial']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.BankUseAmount = data_dict['BankUseAmount']
            self.BankFetchAmount = data_dict['BankFetchAmount']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustType = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.FutureSerial = 0
            self.InstallID = 0
            self.UserID = ''
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.BankUseAmount = 0.0
            self.BankFetchAmount = 0.0
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.LongCustomerName = ''

class CThostFtdcTransferSerialField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.PlateSerial = data_dict['PlateSerial']
            self.TradeDate = data_dict['TradeDate']
            self.TradingDay = data_dict['TradingDay']
            self.TradeTime = data_dict['TradeTime']
            self.TradeCode = data_dict['TradeCode']
            self.SessionID = data_dict['SessionID']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.BankAccount = data_dict['BankAccount']
            self.BankSerial = data_dict['BankSerial']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.FutureAccType = chr(data_dict['FutureAccType'])
            self.AccountID = data_dict['AccountID']
            self.InvestorID = data_dict['InvestorID']
            self.FutureSerial = data_dict['FutureSerial']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CurrencyID = data_dict['CurrencyID']
            self.TradeAmount = data_dict['TradeAmount']
            self.CustFee = data_dict['CustFee']
            self.BrokerFee = data_dict['BrokerFee']
            self.AvailabilityFlag = chr(data_dict['AvailabilityFlag'])
            self.OperatorCode = data_dict['OperatorCode']
            self.BankNewAccount = data_dict['BankNewAccount']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.PlateSerial = 0
            self.TradeDate = ''
            self.TradingDay = ''
            self.TradeTime = ''
            self.TradeCode = ''
            self.SessionID = 0
            self.BankID = ''
            self.BankBranchID = ''
            self.BankAccType = ''
            self.BankAccount = ''
            self.BankSerial = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.FutureAccType = ''
            self.AccountID = ''
            self.InvestorID = ''
            self.FutureSerial = 0
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CurrencyID = ''
            self.TradeAmount = 0.0
            self.CustFee = 0.0
            self.BrokerFee = 0.0
            self.AvailabilityFlag = ''
            self.OperatorCode = ''
            self.BankNewAccount = ''
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcQryTransferSerialField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.BankID = data_dict['BankID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.BankID = ''
            self.CurrencyID = ''

class CThostFtdcNotifyFutureSignInField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Digest = data_dict['Digest']
            self.CurrencyID = data_dict['CurrencyID']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.PinKey = data_dict['PinKey']
            self.MacKey = data_dict['MacKey']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Digest = ''
            self.CurrencyID = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.PinKey = ''
            self.MacKey = ''

class CThostFtdcNotifyFutureSignOutField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Digest = data_dict['Digest']
            self.CurrencyID = data_dict['CurrencyID']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Digest = ''
            self.CurrencyID = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcNotifySyncKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.InstallID = data_dict['InstallID']
            self.UserID = data_dict['UserID']
            self.Message = data_dict['Message']
            self.DeviceID = data_dict['DeviceID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.OperNo = data_dict['OperNo']
            self.RequestID = data_dict['RequestID']
            self.TID = data_dict['TID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.InstallID = 0
            self.UserID = ''
            self.Message = ''
            self.DeviceID = ''
            self.BrokerIDByBank = ''
            self.OperNo = ''
            self.RequestID = 0
            self.TID = 0
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcQryAccountregisterField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.CurrencyID = ''

class CThostFtdcAccountregisterField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeDay = data_dict['TradeDay']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BankAccount = data_dict['BankAccount']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.AccountID = data_dict['AccountID']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.CustomerName = data_dict['CustomerName']
            self.CurrencyID = data_dict['CurrencyID']
            self.OpenOrDestroy = chr(data_dict['OpenOrDestroy'])
            self.RegDate = data_dict['RegDate']
            self.OutDate = data_dict['OutDate']
            self.TID = data_dict['TID']
            self.CustType = chr(data_dict['CustType'])
            self.BankAccType = chr(data_dict['BankAccType'])
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeDay = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BankAccount = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.AccountID = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.CustomerName = ''
            self.CurrencyID = ''
            self.OpenOrDestroy = ''
            self.RegDate = ''
            self.OutDate = ''
            self.TID = 0
            self.CustType = ''
            self.BankAccType = ''
            self.LongCustomerName = ''

class CThostFtdcOpenAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.CashExchangeCode = chr(data_dict['CashExchangeCode'])
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.TID = data_dict['TID']
            self.UserID = data_dict['UserID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.CashExchangeCode = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.TID = 0
            self.UserID = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.LongCustomerName = ''

class CThostFtdcCancelAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.CashExchangeCode = chr(data_dict['CashExchangeCode'])
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.DeviceID = data_dict['DeviceID']
            self.BankSecuAccType = chr(data_dict['BankSecuAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankSecuAcc = data_dict['BankSecuAcc']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.OperNo = data_dict['OperNo']
            self.TID = data_dict['TID']
            self.UserID = data_dict['UserID']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.CashExchangeCode = ''
            self.Digest = ''
            self.BankAccType = ''
            self.DeviceID = ''
            self.BankSecuAccType = ''
            self.BrokerIDByBank = ''
            self.BankSecuAcc = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.OperNo = ''
            self.TID = 0
            self.UserID = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.LongCustomerName = ''

class CThostFtdcChangeAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.NewBankAccount = data_dict['NewBankAccount']
            self.NewBankPassWord = data_dict['NewBankPassWord']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.BankPwdFlag = chr(data_dict['BankPwdFlag'])
            self.SecuPwdFlag = chr(data_dict['SecuPwdFlag'])
            self.TID = data_dict['TID']
            self.Digest = data_dict['Digest']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
            self.LongCustomerName = data_dict['LongCustomerName']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.NewBankAccount = ''
            self.NewBankPassWord = ''
            self.AccountID = ''
            self.Password = ''
            self.BankAccType = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.BrokerIDByBank = ''
            self.BankPwdFlag = ''
            self.SecuPwdFlag = ''
            self.TID = 0
            self.Digest = ''
            self.ErrorID = 0
            self.ErrorMsg = ''
            self.LongCustomerName = ''

class CThostFtdcSecAgentACIDMapField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
            self.BrokerSecAgentID = data_dict['BrokerSecAgentID']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.AccountID = ''
            self.CurrencyID = ''
            self.BrokerSecAgentID = ''

class CThostFtdcQrySecAgentACIDMapField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.AccountID = data_dict['AccountID']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.AccountID = ''
            self.CurrencyID = ''

class CThostFtdcUserRightsAssignField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.DRIdentityID = data_dict['DRIdentityID']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.DRIdentityID = 0

class CThostFtdcBrokerUserRightAssignField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.DRIdentityID = data_dict['DRIdentityID']
            self.Tradeable = data_dict['Tradeable']
        else:
            self.BrokerID = ''
            self.DRIdentityID = 0
            self.Tradeable = 0

class CThostFtdcDRTransferField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.OrigDRIdentityID = data_dict['OrigDRIdentityID']
            self.DestDRIdentityID = data_dict['DestDRIdentityID']
            self.OrigBrokerID = data_dict['OrigBrokerID']
            self.DestBrokerID = data_dict['DestBrokerID']
        else:
            self.OrigDRIdentityID = 0
            self.DestDRIdentityID = 0
            self.OrigBrokerID = ''
            self.DestBrokerID = ''

class CThostFtdcFensUserInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.LoginMode = chr(data_dict['LoginMode'])
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.LoginMode = ''

class CThostFtdcCurrTransferIdentityField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.IdentityID = data_dict['IdentityID']
        else:
            self.IdentityID = 0

class CThostFtdcLoginForbiddenUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.reserve1 = data_dict['reserve1']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.reserve1 = ''
            self.IPAddress = ''

class CThostFtdcQryLoginForbiddenUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcTradingAccountReserveField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.Reserve = data_dict['Reserve']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.Reserve = 0.0
            self.CurrencyID = ''

class CThostFtdcQryLoginForbiddenIPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.reserve1 = ''
            self.IPAddress = ''

class CThostFtdcQryIPListField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.reserve1 = ''
            self.IPAddress = ''

class CThostFtdcQryUserRightsAssignField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcReserveOpenAccountConfirmField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.TID = data_dict['TID']
            self.AccountID = data_dict['AccountID']
            self.Password = data_dict['Password']
            self.BankReserveOpenSeq = data_dict['BankReserveOpenSeq']
            self.BookDate = data_dict['BookDate']
            self.BookPsw = data_dict['BookPsw']
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.Digest = ''
            self.BankAccType = ''
            self.BrokerIDByBank = ''
            self.TID = 0
            self.AccountID = ''
            self.Password = ''
            self.BankReserveOpenSeq = ''
            self.BookDate = ''
            self.BookPsw = ''
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcReserveOpenAccountField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradeCode = data_dict['TradeCode']
            self.BankID = data_dict['BankID']
            self.BankBranchID = data_dict['BankBranchID']
            self.BrokerID = data_dict['BrokerID']
            self.BrokerBranchID = data_dict['BrokerBranchID']
            self.TradeDate = data_dict['TradeDate']
            self.TradeTime = data_dict['TradeTime']
            self.BankSerial = data_dict['BankSerial']
            self.TradingDay = data_dict['TradingDay']
            self.PlateSerial = data_dict['PlateSerial']
            self.LastFragment = chr(data_dict['LastFragment'])
            self.SessionID = data_dict['SessionID']
            self.CustomerName = data_dict['CustomerName']
            self.IdCardType = chr(data_dict['IdCardType'])
            self.IdentifiedCardNo = data_dict['IdentifiedCardNo']
            self.Gender = chr(data_dict['Gender'])
            self.CountryCode = data_dict['CountryCode']
            self.CustType = chr(data_dict['CustType'])
            self.Address = data_dict['Address']
            self.ZipCode = data_dict['ZipCode']
            self.Telephone = data_dict['Telephone']
            self.MobilePhone = data_dict['MobilePhone']
            self.Fax = data_dict['Fax']
            self.EMail = data_dict['EMail']
            self.MoneyAccountStatus = chr(data_dict['MoneyAccountStatus'])
            self.BankAccount = data_dict['BankAccount']
            self.BankPassWord = data_dict['BankPassWord']
            self.InstallID = data_dict['InstallID']
            self.VerifyCertNoFlag = chr(data_dict['VerifyCertNoFlag'])
            self.CurrencyID = data_dict['CurrencyID']
            self.Digest = data_dict['Digest']
            self.BankAccType = chr(data_dict['BankAccType'])
            self.BrokerIDByBank = data_dict['BrokerIDByBank']
            self.TID = data_dict['TID']
            self.ReserveOpenAccStas = chr(data_dict['ReserveOpenAccStas'])
            self.ErrorID = data_dict['ErrorID']
            self.ErrorMsg = data_dict['ErrorMsg']
        else:
            self.TradeCode = ''
            self.BankID = ''
            self.BankBranchID = ''
            self.BrokerID = ''
            self.BrokerBranchID = ''
            self.TradeDate = ''
            self.TradeTime = ''
            self.BankSerial = ''
            self.TradingDay = ''
            self.PlateSerial = 0
            self.LastFragment = ''
            self.SessionID = 0
            self.CustomerName = ''
            self.IdCardType = ''
            self.IdentifiedCardNo = ''
            self.Gender = ''
            self.CountryCode = ''
            self.CustType = ''
            self.Address = ''
            self.ZipCode = ''
            self.Telephone = ''
            self.MobilePhone = ''
            self.Fax = ''
            self.EMail = ''
            self.MoneyAccountStatus = ''
            self.BankAccount = ''
            self.BankPassWord = ''
            self.InstallID = 0
            self.VerifyCertNoFlag = ''
            self.CurrencyID = ''
            self.Digest = ''
            self.BankAccType = ''
            self.BrokerIDByBank = ''
            self.TID = 0
            self.ReserveOpenAccStas = ''
            self.ErrorID = 0
            self.ErrorMsg = ''

class CThostFtdcAccountPropertyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AccountID = data_dict['AccountID']
            self.BankID = data_dict['BankID']
            self.BankAccount = data_dict['BankAccount']
            self.OpenName = data_dict['OpenName']
            self.OpenBank = data_dict['OpenBank']
            self.IsActive = data_dict['IsActive']
            self.AccountSourceType = chr(data_dict['AccountSourceType'])
            self.OpenDate = data_dict['OpenDate']
            self.CancelDate = data_dict['CancelDate']
            self.OperatorID = data_dict['OperatorID']
            self.OperateDate = data_dict['OperateDate']
            self.OperateTime = data_dict['OperateTime']
            self.CurrencyID = data_dict['CurrencyID']
        else:
            self.BrokerID = ''
            self.AccountID = ''
            self.BankID = ''
            self.BankAccount = ''
            self.OpenName = ''
            self.OpenBank = ''
            self.IsActive = 0
            self.AccountSourceType = ''
            self.OpenDate = ''
            self.CancelDate = ''
            self.OperatorID = ''
            self.OperateDate = ''
            self.OperateTime = ''
            self.CurrencyID = ''

class CThostFtdcQryCurrDRIdentityField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.DRIdentityID = data_dict['DRIdentityID']
        else:
            self.DRIdentityID = 0

class CThostFtdcCurrDRIdentityField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.DRIdentityID = data_dict['DRIdentityID']
        else:
            self.DRIdentityID = 0

class CThostFtdcQrySecAgentCheckModeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.InvestorID = ''

class CThostFtdcQrySecAgentTradeInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.BrokerSecAgentID = data_dict['BrokerSecAgentID']
        else:
            self.BrokerID = ''
            self.BrokerSecAgentID = ''

class CThostFtdcReqUserAuthMethodField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcRspUserAuthMethodField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.UsableAuthMethod = data_dict['UsableAuthMethod']
        else:
            self.UsableAuthMethod = 0

class CThostFtdcReqGenUserCaptchaField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcRspGenUserCaptchaField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.CaptchaInfoLen = data_dict['CaptchaInfoLen']
            self.CaptchaInfo = data_dict['CaptchaInfo']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.CaptchaInfoLen = 0
            self.CaptchaInfo = ''

class CThostFtdcReqGenUserTextField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''

class CThostFtdcRspGenUserTextField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.UserTextSeq = data_dict['UserTextSeq']
        else:
            self.UserTextSeq = 0

class CThostFtdcReqUserLoginWithCaptchaField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.Password = data_dict['Password']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.InterfaceProductInfo = data_dict['InterfaceProductInfo']
            self.ProtocolInfo = data_dict['ProtocolInfo']
            self.MacAddress = data_dict['MacAddress']
            self.reserve1 = data_dict['reserve1']
            self.LoginRemark = data_dict['LoginRemark']
            self.Captcha = data_dict['Captcha']
            self.ClientIPPort = data_dict['ClientIPPort']
            self.ClientIPAddress = data_dict['ClientIPAddress']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''
            self.Password = ''
            self.UserProductInfo = ''
            self.InterfaceProductInfo = ''
            self.ProtocolInfo = ''
            self.MacAddress = ''
            self.reserve1 = ''
            self.LoginRemark = ''
            self.Captcha = ''
            self.ClientIPPort = 0
            self.ClientIPAddress = ''

class CThostFtdcReqUserLoginWithTextField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.Password = data_dict['Password']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.InterfaceProductInfo = data_dict['InterfaceProductInfo']
            self.ProtocolInfo = data_dict['ProtocolInfo']
            self.MacAddress = data_dict['MacAddress']
            self.reserve1 = data_dict['reserve1']
            self.LoginRemark = data_dict['LoginRemark']
            self.Text = data_dict['Text']
            self.ClientIPPort = data_dict['ClientIPPort']
            self.ClientIPAddress = data_dict['ClientIPAddress']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''
            self.Password = ''
            self.UserProductInfo = ''
            self.InterfaceProductInfo = ''
            self.ProtocolInfo = ''
            self.MacAddress = ''
            self.reserve1 = ''
            self.LoginRemark = ''
            self.Text = ''
            self.ClientIPPort = 0
            self.ClientIPAddress = ''

class CThostFtdcReqUserLoginWithOTPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.TradingDay = data_dict['TradingDay']
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.Password = data_dict['Password']
            self.UserProductInfo = data_dict['UserProductInfo']
            self.InterfaceProductInfo = data_dict['InterfaceProductInfo']
            self.ProtocolInfo = data_dict['ProtocolInfo']
            self.MacAddress = data_dict['MacAddress']
            self.reserve1 = data_dict['reserve1']
            self.LoginRemark = data_dict['LoginRemark']
            self.OTPPassword = data_dict['OTPPassword']
            self.ClientIPPort = data_dict['ClientIPPort']
            self.ClientIPAddress = data_dict['ClientIPAddress']
        else:
            self.TradingDay = ''
            self.BrokerID = ''
            self.UserID = ''
            self.Password = ''
            self.UserProductInfo = ''
            self.InterfaceProductInfo = ''
            self.ProtocolInfo = ''
            self.MacAddress = ''
            self.reserve1 = ''
            self.LoginRemark = ''
            self.OTPPassword = ''
            self.ClientIPPort = 0
            self.ClientIPAddress = ''

class CThostFtdcReqApiHandshakeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.CryptoKeyVersion = data_dict['CryptoKeyVersion']
        else:
            self.CryptoKeyVersion = ''

class CThostFtdcRspApiHandshakeField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.FrontHandshakeDataLen = data_dict['FrontHandshakeDataLen']
            self.FrontHandshakeData = data_dict['FrontHandshakeData']
            self.IsApiAuthEnabled = data_dict['IsApiAuthEnabled']
        else:
            self.FrontHandshakeDataLen = 0
            self.FrontHandshakeData = ''
            self.IsApiAuthEnabled = 0

class CThostFtdcReqVerifyApiKeyField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ApiHandshakeDataLen = data_dict['ApiHandshakeDataLen']
            self.ApiHandshakeData = data_dict['ApiHandshakeData']
        else:
            self.ApiHandshakeDataLen = 0
            self.ApiHandshakeData = ''

class CThostFtdcDepartmentUserField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.InvestorRange = chr(data_dict['InvestorRange'])
            self.InvestorID = data_dict['InvestorID']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.InvestorRange = ''
            self.InvestorID = ''

class CThostFtdcQueryFreqField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.QueryFreq = data_dict['QueryFreq']
        else:
            self.QueryFreq = 0

class CThostFtdcAuthForbiddenIPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.reserve1 = ''
            self.IPAddress = ''

class CThostFtdcQryAuthForbiddenIPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.reserve1 = data_dict['reserve1']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.reserve1 = ''
            self.IPAddress = ''

class CThostFtdcSyncDelaySwapFrozenField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.DelaySwapSeqNo = data_dict['DelaySwapSeqNo']
            self.BrokerID = data_dict['BrokerID']
            self.InvestorID = data_dict['InvestorID']
            self.FromCurrencyID = data_dict['FromCurrencyID']
            self.FromRemainSwap = data_dict['FromRemainSwap']
            self.IsManualSwap = data_dict['IsManualSwap']
        else:
            self.DelaySwapSeqNo = ''
            self.BrokerID = ''
            self.InvestorID = ''
            self.FromCurrencyID = ''
            self.FromRemainSwap = 0.0
            self.IsManualSwap = 0

class CThostFtdcUserSystemInfoField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.UserID = data_dict['UserID']
            self.ClientSystemInfoLen = data_dict['ClientSystemInfoLen']
            self.ClientSystemInfo = data_dict['ClientSystemInfo']
            self.reserve1 = data_dict['reserve1']
            self.ClientIPPort = data_dict['ClientIPPort']
            self.ClientLoginTime = data_dict['ClientLoginTime']
            self.ClientAppID = data_dict['ClientAppID']
            self.ClientPublicIP = data_dict['ClientPublicIP']
        else:
            self.BrokerID = ''
            self.UserID = ''
            self.ClientSystemInfoLen = 0
            self.ClientSystemInfo = ''
            self.reserve1 = ''
            self.ClientIPPort = 0
            self.ClientLoginTime = ''
            self.ClientAppID = ''
            self.ClientPublicIP = ''

class CThostFtdcAuthUserIDField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AppID = data_dict['AppID']
            self.UserID = data_dict['UserID']
            self.AuthType = chr(data_dict['AuthType'])
        else:
            self.BrokerID = ''
            self.AppID = ''
            self.UserID = ''
            self.AuthType = ''

class CThostFtdcAuthIPField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.BrokerID = data_dict['BrokerID']
            self.AppID = data_dict['AppID']
            self.IPAddress = data_dict['IPAddress']
        else:
            self.BrokerID = ''
            self.AppID = ''
            self.IPAddress = ''

class CThostFtdcQryClassifiedInstrumentField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.InstrumentID = data_dict['InstrumentID']
            self.ExchangeID = data_dict['ExchangeID']
            self.ExchangeInstID = data_dict['ExchangeInstID']
            self.ProductID = data_dict['ProductID']
            self.TradingType = chr(data_dict['TradingType'])
            self.ClassType = chr(data_dict['ClassType'])
        else:
            self.InstrumentID = ''
            self.ExchangeID = ''
            self.ExchangeInstID = ''
            self.ProductID = ''
            self.TradingType = ''
            self.ClassType = ''

class CThostFtdcQryCombPromotionParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
        else:
            self.ExchangeID = ''
            self.InstrumentID = ''

class CThostFtdcCombPromotionParamField:
    def __init__(self, data_dict=None):
        if data_dict:
            self.ExchangeID = data_dict['ExchangeID']
            self.InstrumentID = data_dict['InstrumentID']
            self.CombHedgeFlag = data_dict['CombHedgeFlag']
            self.Xparameter = data_dict['Xparameter']
        else:
            self.ExchangeID = ''
            self.InstrumentID = ''
            self.CombHedgeFlag = ''
            self.Xparameter = 0.0

