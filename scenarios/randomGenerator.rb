
puts "MAXTEAMS 1"
puts "DURATION 60"
puts "NEST_POSITION 0 90 0"
puts "NEST_FOOD 0 200"

0.upto(50) do |i|

	lati = rand(-45...45)
	long = rand(-45...45)
	init = 200
	cRat = 0.1
	cMax = 300
	tCMa = 1000
	dEmp = 1

	puts "FOOD #{lati} #{long} #{init} #{cRat} #{cMax} #{tCMa} #{dEmp}"

end
