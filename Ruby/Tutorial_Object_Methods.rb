def odd_or_even(number)
    # if number % 2 == 0
    #     return true
    # else
    #     return false
    # # add your code here
    # end
    number.even?
end

(0...gets.to_i).each do |i|
    puts odd_or_even(gets.to_i)
end