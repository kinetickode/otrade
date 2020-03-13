# tests
import pytest
from otrade.utils.safe_robin_stocks import safe_robin_stocks, NO_OP_RESULT

def test_safe_robin_stocks():
    expected_result = NO_OP_RESULT
    assert safe_robin_stocks.cancel_all_open_orders() == expected_result
    assert safe_robin_stocks.cancel_order() == expected_result
    assert safe_robin_stocks.find_orders() == expected_result
    assert safe_robin_stocks.find_tradable_options_for_stock() == expected_result
    assert safe_robin_stocks.get_bank_account_info() == expected_result
    assert safe_robin_stocks.get_bank_transfers() == expected_result
    assert safe_robin_stocks.get_chains() == expected_result
    assert safe_robin_stocks.get_all_orders() == expected_result
    assert safe_robin_stocks.get_linked_bank_accounts() == expected_result
    assert safe_robin_stocks.get_watchlist_by_name() == expected_result
    assert safe_robin_stocks.get_wire_transfers() == expected_result
    assert safe_robin_stocks.globals() == expected_result
    assert safe_robin_stocks.helper() == expected_result
    assert safe_robin_stocks.load_account_profile() == expected_result
    assert safe_robin_stocks.load_basic_profile() == expected_result
    assert safe_robin_stocks.load_crypto_profile() == expected_result
    assert safe_robin_stocks.load_investment_profile() == expected_result
    assert safe_robin_stocks.load_portfolio_profile() == expected_result
    assert safe_robin_stocks.load_security_profile() == expected_result
    assert safe_robin_stocks.load_user_profile() == expected_result
    assert safe_robin_stocks.order() == expected_result
    assert safe_robin_stocks.order_buy_crypto_by_price() == expected_result
    assert safe_robin_stocks.order_buy_crypto_by_quantity() == expected_result
    assert safe_robin_stocks.order_buy_limit() == expected_result
    assert safe_robin_stocks.order_buy_market() == expected_result
    assert safe_robin_stocks.order_buy_option_limit() == expected_result
    assert safe_robin_stocks.order_buy_stop_limit() == expected_result
    assert safe_robin_stocks.order_buy_stop_loss() == expected_result
    assert safe_robin_stocks.order_option_credit_spread() == expected_result
    assert safe_robin_stocks.order_option_debit_spread() == expected_result
    assert safe_robin_stocks.order_option_spread() == expected_result
    assert safe_robin_stocks.order_sell_crypto_by_price() == expected_result
    assert safe_robin_stocks.order_sell_crypto_by_quantity() == expected_result
    assert safe_robin_stocks.order_sell_limit() == expected_result
    assert safe_robin_stocks.order_sell_market() == expected_result
    assert safe_robin_stocks.order_sell_option_limit() == expected_result
    assert safe_robin_stocks.order_sell_stop_limit() == expected_result
    assert safe_robin_stocks.order_sell_stop_loss() == expected_result
    assert safe_robin_stocks.orders() == expected_result
    assert safe_robin_stocks.post_symbols_to_watchlist() == expected_result
    assert safe_robin_stocks.request_delete() == expected_result
    assert safe_robin_stocks.request_document() == expected_result
    assert safe_robin_stocks.unlink_bank_account() == expected_result
    assert safe_robin_stocks.update_session() == expected_result
