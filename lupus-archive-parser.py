archive_Data = open('8x.text', 'r')
archive_File = open('lupus-2014-archive-tester.text', 'a')

# count = 0
for line in archive_Data:
    for tweet in line.split('),('):
        if 'lupus' in tweet:
            print(tweet)
            # count += 1
            archive_File.write(tweet)
            archive_File.write("),(")
        if 'LUPUS' in tweet:
            print(tweet)
            archive_File.write(tweet)
            archive_File.write("),(")

    # if count > 10:
        # break

archive_File.close()
archive_Data.close()
