package money;

import java.util.Objects;

public class Money implements Expression {

    final int amount;
    final String currency;

    public Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    String currency() {
        return currency;
    }

    public Expression times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }

    public Expression plus(Expression addend) {
        return new Sum(this, addend);
    }

    @Override
    public Money reduce(Bank bank, String to) {
        int rate = bank.rate(currency, to);
        return new Money(amount / rate, to);
    }

    @Override
    public boolean equals(Object object) {
        return object instanceof Money && ((Money) object).amount == amount
                && Objects.equals(((Money)object).currency, currency);
    }

    @Override
    public String toString() {
        return amount + " " + currency;
    }

    public static Money dollar(int amount) {
        return new Money(amount, "USD");
    }

    public static Money franc(int amount) {
        return new Money(amount, "CHF");
    }

}
