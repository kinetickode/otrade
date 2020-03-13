import robin_stocks

NO_OP_RESULT = 'Sanitized for your protection.'


def no_op():
    return NO_OP_RESULT


safe_robin_stocks = robin_stocks

# no_op functions that can get us into trouble
safe_robin_stocks.cancel_all_open_orders = no_op
safe_robin_stocks.cancel_order = no_op
safe_robin_stocks.find_orders = no_op
safe_robin_stocks.find_tradable_options_for_stock = no_op
safe_robin_stocks.get_bank_account_info = no_op
safe_robin_stocks.get_bank_transfers = no_op
safe_robin_stocks.get_chains = no_op
safe_robin_stocks.get_all_orders = no_op
safe_robin_stocks.get_linked_bank_accounts = no_op
safe_robin_stocks.get_watchlist_by_name = no_op
safe_robin_stocks.get_wire_transfers = no_op
safe_robin_stocks.globals = no_op
safe_robin_stocks.helper = no_op
safe_robin_stocks.load_account_profile = no_op
safe_robin_stocks.load_basic_profile = no_op
safe_robin_stocks.load_crypto_profile = no_op
safe_robin_stocks.load_investment_profile = no_op
safe_robin_stocks.load_portfolio_profile = no_op
safe_robin_stocks.load_security_profile = no_op
safe_robin_stocks.load_user_profile = no_op
safe_robin_stocks.order = no_op
safe_robin_stocks.order_buy_crypto_by_price = no_op
safe_robin_stocks.order_buy_crypto_by_quantity = no_op
safe_robin_stocks.order_buy_limit = no_op
safe_robin_stocks.order_buy_market = no_op
safe_robin_stocks.order_buy_option_limit = no_op
safe_robin_stocks.order_buy_stop_limit = no_op
safe_robin_stocks.order_buy_stop_loss = no_op
safe_robin_stocks.order_option_credit_spread = no_op
safe_robin_stocks.order_option_debit_spread = no_op
safe_robin_stocks.order_option_spread = no_op
safe_robin_stocks.order_sell_crypto_by_price = no_op
safe_robin_stocks.order_sell_crypto_by_quantity = no_op
safe_robin_stocks.order_sell_limit = no_op
safe_robin_stocks.order_sell_market = no_op
safe_robin_stocks.order_sell_option_limit = no_op
safe_robin_stocks.order_sell_stop_limit = no_op
safe_robin_stocks.order_sell_stop_loss = no_op
safe_robin_stocks.orders = no_op
safe_robin_stocks.post_symbols_to_watchlist = no_op
safe_robin_stocks.request_delete = no_op
safe_robin_stocks.request_document = no_op
safe_robin_stocks.unlink_bank_account = no_op
safe_robin_stocks.update_session = no_op
