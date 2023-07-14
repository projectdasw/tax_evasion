# oTree apps

Some experimental implementation of games for oTree v5

## Real-effort tasks

Games:
- `transcription`: transcribing of distorted text from image
- `matrices`: counting symbols in matrix
- `decoding`: decoding a letters/numbers cipher 
- `sliders`: moving sliders task

The task units are referenced as 'puzzles' in docs and code.

All games are impemented as single-user, single page apps.

Common features:
- live page with infinite iterations (micro-rounds) and timeout
- generating randomized puzzle on the fly
- creating images for each puzzle on the fly
- showing the images on the live page
- recording outcome of each puzzle in database
- custom export of all recorded data

Anti-cheating and anti-scripting protection:
- the puzzles are generated as images, no solution data is even revealed into browser
- validation of answers on server side
- `puzzle_delay`: minimal delay between iterations
- `retry_delay`: minimal delay before next retry after wrong answer 

Configurable features, via session config:
- `attempts_per_puzzle`: number of attempts allowed to solve puzzle 
- `max_iterations`: complete round after given number of iterations.
  (if timeout is also specified for a page, round is terminated by whichever comes first.)
  
For sliders:
- `num_sliders`: total number of sliders
- `num_columns`: number of columns in grid

More detailed adjustments are available via variables in files `task_something.py`
