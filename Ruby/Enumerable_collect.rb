
#実験
#-----------------------
# print({:a=>1, :b=>2, :c=>3}.collect { |key, value| 2*value })
# (1..3).reverse_each { |val| puts val }
# puts [5,5,4].all? { |v| v == 5 }
# puts [2,4,5].any? { |v| v == 5 }
# puts 2.range? 3,4
# print([1,2,3].collect { |v| v * 2 })

# def rot13(secret_messages)
#     puts secret_messages[3]
#     print([1,2,3].map { |x| 2*x })
#     secret_messages.map { |c| c.tr("a-z", "n-za-m") }
# end
#---------------------------------


# part1
# def rot13(secret_messages)
# 	# your code here
# 	secret_messages.collect { |str| str.tr('A-Za-z', 'N-ZA-Mn-za-m')}
# end

#part2
def rot13(secret_messages)

    secret_messages.map { |c| c.tr("a-z", "n-za-m") }
end

puts (rot13("Why did the chicken cross the road?"))