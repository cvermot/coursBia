$pdf_mode = 4; #Force PDF
#$pdflatex = 'lualatex %O %S'; # Forcer LuaLaTeX

add_cus_dep( 'acn', 'acr', 0, 'makeglossaries' );
add_cus_dep( 'glo', 'gls', 0, 'makeglossaries' );
#set_tex_cmds( '--shell-escape %O %S' ); #Non nécessaire si pas de compilation externe
$clean_ext .= " acr acn alg glo gls glg";
sub makeglossaries {
  my ($base_name, $path) = fileparse( $_[0] );
  pushd $path;
  my $return = system "makeglossaries", $base_name;
  popd;
  return $return;
}
