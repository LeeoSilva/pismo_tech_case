import factory
import slugify

from src.models import Account, OperationType, Transaction


class TransactionFactory(factory.Factory):
    class Meta:
        model = Transaction

    account_id = factory.Sequence(lambda n: n + 1)
    operation_type_id = factory.Sequence(lambda n: n + 1)
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    created_at = factory.Faker("date_time_this_year", tzinfo=None)


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    document_number = factory.Faker("cpf", locale="pt_BR")
    account_limit = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )
    created_at = factory.Faker("date_time_this_year", tzinfo=None)


class OperationTypeFactory(factory.Factory):
    class Meta:
        model = OperationType

    description = factory.Faker("word")
    slug = factory.LazyAttribute(
        lambda obj: slugify.slugify(obj.description, separator="_")
    )
    created_at = factory.Faker("date_time_this_year", tzinfo=None)
