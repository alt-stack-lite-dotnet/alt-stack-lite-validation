```

BenchmarkDotNet v0.14.0, Windows 11 (10.0.26200.8037)
13th Gen Intel Core i7-13650HX, 1 CPU, 20 logical and 14 physical cores
.NET SDK 10.0.100
  [Host]     : .NET 10.0.0 (10.0.25.52411), X64 RyuJIT AVX2
  Job-OGWUDH : .NET 10.0.0 (10.0.25.52411), X64 RyuJIT AVX2
  ShortRun   : .NET 10.0.0 (10.0.25.52411), X64 RyuJIT AVX2

WarmupCount=3  

```
| Method                   | Job        | IterationCount | LaunchCount | Mean          | Error         | StdDev      | Ratio  | RatioSD | Gen0   | Gen1   | Allocated | Alloc Ratio |
|------------------------- |----------- |--------------- |------------ |--------------:|--------------:|------------:|-------:|--------:|-------:|-------:|----------:|------------:|
| FluentValidation_Valid   | Job-OGWUDH | 10             | Default     |   426.2361 ns |     8.9991 ns |   5.3552 ns |  1.000 |    0.02 | 0.0527 |      - |     664 B |        1.00 |
| FluentValidation_Invalid | Job-OGWUDH | 10             | Default     | 2,782.4244 ns |    54.2009 ns |  35.8505 ns |  6.529 |    0.11 | 0.7133 | 0.0038 |    8952 B |       13.48 |
| LiteRuntime_Valid        | Job-OGWUDH | 10             | Default     |     0.6560 ns |     0.0511 ns |   0.0267 ns |  0.002 |    0.00 |      - |      - |         - |        0.00 |
| LiteRuntime_Invalid      | Job-OGWUDH | 10             | Default     |     1.2299 ns |     0.0928 ns |   0.0485 ns |  0.003 |    0.00 |      - |      - |         - |        0.00 |
| LiteSg_Valid             | Job-OGWUDH | 10             | Default     |    14.2847 ns |     0.1837 ns |   0.1215 ns |  0.034 |    0.00 |      - |      - |         - |        0.00 |
| LiteSg_Invalid           | Job-OGWUDH | 10             | Default     |    30.5776 ns |    11.0054 ns |   7.2794 ns |  0.072 |    0.02 | 0.0095 |      - |     120 B |        0.18 |
| DataAnnotations_Valid    | Job-OGWUDH | 10             | Default     |   941.1896 ns |    35.3764 ns |  23.3993 ns |  2.208 |    0.06 | 0.1440 |      - |    1816 B |        2.73 |
| DataAnnotations_Invalid  | Job-OGWUDH | 10             | Default     | 1,515.3218 ns |    29.2841 ns |  15.3162 ns |  3.556 |    0.05 | 0.1898 | 0.0010 |    2384 B |        3.59 |
|                          |            |                |             |               |               |             |        |         |        |        |           |             |
| FluentValidation_Valid   | ShortRun   | 3              | 1           |   427.1737 ns |   118.7737 ns |   6.5104 ns |  1.000 |    0.02 | 0.0527 |      - |     664 B |        1.00 |
| FluentValidation_Invalid | ShortRun   | 3              | 1           | 4,561.4009 ns | 2,356.4141 ns | 129.1630 ns | 10.680 |    0.30 | 0.7133 | 0.0038 |    8952 B |       13.48 |
| LiteRuntime_Valid        | ShortRun   | 3              | 1           |     0.5914 ns |     0.2629 ns |   0.0144 ns |  0.001 |    0.00 |      - |      - |         - |        0.00 |
| LiteRuntime_Invalid      | ShortRun   | 3              | 1           |     1.4190 ns |     2.2312 ns |   0.1223 ns |  0.003 |    0.00 |      - |      - |         - |        0.00 |
| LiteSg_Valid             | ShortRun   | 3              | 1           |    14.1681 ns |     9.9015 ns |   0.5427 ns |  0.033 |    0.00 |      - |      - |         - |        0.00 |
| LiteSg_Invalid           | ShortRun   | 3              | 1           |    34.2483 ns |    10.4103 ns |   0.5706 ns |  0.080 |    0.00 | 0.0095 |      - |     120 B |        0.18 |
| DataAnnotations_Valid    | ShortRun   | 3              | 1           |   881.3582 ns |   299.2465 ns |  16.4027 ns |  2.064 |    0.04 | 0.1440 |      - |    1816 B |        2.73 |
| DataAnnotations_Invalid  | ShortRun   | 3              | 1           | 1,477.5955 ns |   417.0084 ns |  22.8576 ns |  3.460 |    0.07 | 0.1898 | 0.0010 |    2384 B |        3.59 |
