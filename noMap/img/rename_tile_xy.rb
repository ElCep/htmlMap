tile_width = 500
tile_height = 500
image_width = 4032
image_height = 3024
n = 0
# il faudra connaitre le nombre d''image généré
# on regarde le nombre incrémenter par convret auquel on ajoute 1
# e.g. tiles_99.png => total_tiles = 100
total_tiles = 63

tiles_per_column = image_width/tile_width

row = 0
column = 0
(n...total_tiles).each do |i|
  filename = "tiles_#{i}.png" # current filename
  target = "map_#{column}_#{row}.png" # new filename

  puts "copy #{filename} to #{target}"

  `cp -f #{filename} #{target}` # rename

  # work out next step
  column = column + 1
  if column >= tiles_per_column
    column = 0
    row = row + 1
  end
end
