$pdf_mode = 5;
$do_cd = 1;
$aux_dir = '.build';
$clean_ext .= ' nav snm';

# Share the paper's bibliography, including when BibTeX runs inside .build/.
use Cwd qw(abs_path);
use File::Basename qw(dirname);
my $slides_dir = dirname(abs_path(__FILE__));
ensure_path('BIBINPUTS', abs_path("$slides_dir/../paper"));
