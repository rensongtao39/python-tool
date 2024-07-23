

def get_management_console_address(seller_id):
    # Step 1: Get the shard
    shard = seller_id[-2:]

    # Step 2: Check if shard is a valid hex digit
    try:
        int(shard, 16)
    except ValueError:
        return f"{shard} 输入内容有误请检查"


    # Step 3: Determine the management console address based on the shard range
    shard_ranges = {
        '00-1f': 'https://ddl.dhgateinternal.com/readonly/slave_query/84/',
        '20-3f': 'https://ddl.dhgateinternal.com/readonly/slave_query/914/',
        '40-5f': 'https://ddl.dhgateinternal.com/readonly/slave_query/85/',
        '60-7f': 'https://ddl.dhgateinternal.com/readonly/slave_query/915/',
        '80-9f': 'https://ddl.dhgateinternal.com/readonly/slave_query/86/',
        'a0-bf': 'https://ddl.dhgateinternal.com/readonly/slave_query/916/',
        'c0-df': 'https://ddl.dhgateinternal.com/readonly/slave_query/87/',
        'e0-ff': 'https://ddl.dhgateinternal.com/readonly/slave_query/917/'
    }

    # Convert hex ranges to decimal for comparison
    shard_decimal = int(shard, 16)

    for range_key, url in shard_ranges.items():

        start_range, end_range = range_key.split('-')
        if int(start_range, 16) <= shard_decimal <= int(end_range, 16):
            print(f"Shard: {shard}, Range: {range_key}, URL: {url}")
            print(f"sql: select * from product_{shard} where supplierid = '{seller_id}'")
            return f"<a href='{url}'>{url}</a>"

    # In case of some unexpected shard value not accounted for
    return f"{shard} 输入内容有误请检查"

# Example usage
seller_id_input = "ff8080814999ac040149da3d4608298d"
print(get_management_console_address(seller_id_input))



print("<------------------------------------------------------------------------------------------------>")

if __name__ == '__main__':

    seller_id =  input('卖家ID: ')
    print(get_management_console_address(seller_id))
