a,b,c,d = gets.split.map(&:to_i)

def selectTest(a,b,c,d)
	if a.even? == true and d > a and b > c and (c+d) > (a+b) and d > 0 and c > 0
			return "Valores aceitos"
	else
		return "Valores nao aceitos"
	end
end

puts selectTest(a,b,c,d)
