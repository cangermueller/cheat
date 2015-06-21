plot_heat <- function(d) {
  colors <- rev(brewer.pal(9, 'Spectral'))
  colors <- colorRampPalette(colors)(50)

  p <- heatmap.2(d, density.info='none', trace='none',
    col=colors, labRow=NA, Colv=T, keysize=1.0, dendro='column',
    lwid=c(2, 5), key.title='', srtCol=45)
}


