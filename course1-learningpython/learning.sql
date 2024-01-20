'''migration practice'''
#this is an example of an up migration
#a down migration would be reverting an up migration made


ALTER TABLE transactions
ADD COLUMN was_successful BOOLEAN;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT;

