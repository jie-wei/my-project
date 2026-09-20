$pdf_mode = 5;
$do_cd    = 1;
$aux_dir  = '.build';
$success_cmd = '[ "%R" = "main" ] && cp .build/main.aux main.aux 2>/dev/null; rm -rf .build && rm -f %R.bbl %R.blg %R.brf %R.fdb_latexmk %R.fls %R.log %R.out %R.synctex.gz %R.toc';

use Cwd qw(abs_path);
use File::Basename qw(dirname);
my $paper_dir = dirname(abs_path(__FILE__));
my $templates = abs_path("$paper_dir/../docs/templates/latex");

ensure_path('TEXINPUTS', "$paper_dir//:$templates//:.");
ensure_path('BIBINPUTS', "$paper_dir//:$templates//:.");
ensure_path('BSTINPUTS', "$paper_dir//:$templates//:.");
