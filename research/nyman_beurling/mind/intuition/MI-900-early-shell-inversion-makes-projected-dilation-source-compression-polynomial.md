# MI-900 — Farey separation makes projected-dilation source compression quadratic

**Evidence level:** proved source-compression bounds from [NB-300](../../findings/NB-300-reciprocal-cell-periodicity-gives-explicit-moving-cutoff-source-compression.md), [NB-301](../../findings/NB-301-early-shell-mobius-inversion-gives-cubic-moving-cutoff-source-compression.md), [NB-302](../../findings/NB-302-pairwise-shell-periodicity-lowers-moving-cutoff-source-compression-to-five-halves.md), and the stronger [NB-303](../../findings/NB-303-farey-separated-shell-frequencies-force-quadratic-moving-cutoff-source-compression.md), combined with the exact projected-dilation factorization of NB-297--NB-299.

The large-dilation obstruction is not tied to the exponential reciprocal-cell period. For `U_N=span{g_2,...,g_N}`, write the reciprocal-shell sequence as `u_k=sum_(j=2)^N a_j (k mod j)/j`. NB-301 used the first `N` shells and finite Möbius inversion to reduce the NB-300 lcm-scale criterion to the cubic sufficient condition `m/N^3 -> infinity`. NB-302 then exploited pairwise periods `lcm(i,j)<=N^2` inside the quadratic tail form and pushed the sufficient scale to `m/N^(5/2) -> infinity`.

NB-303 identifies the stronger global structure behind those pairwise periods. Every shell sequence is a finite trigonometric polynomial whose distinct frequencies are reduced rationals of denominator at most `N`; hence they are separated on `R/Z` by at least `N^(-2)`. The Montgomery--Vaughan separated-frequency large sieve therefore gives, on every interval `I` of `L` consecutive shells,

`sum_(k in I)|u_k|^2 <= (L+N^2) Q_N(u)`,

where `Q_N(u)` is the Cesàro shell energy. Exact orthogonality over the common period `P_N=lcm(2,...,N)`, followed by a large-sieve bound on the complement of the first `2N^2` shells, yields the uniform source estimate

`Q_N(u) <= (4N^2+2)||u||_2^2 <= 5N^2||u||_2^2`.

Applying the same interval estimate dyadically to the weighted tail gives

`||1_(0,1/m]u||_2^2 <= [10N^2/m + 20N^4/(3m^2)] ||u||_2^2`.

Hence the projected-dilation overlap now satisfies

`beta_(N+1)(m)^2 <= min(1, 10N^2/m + 20N^4/(3m^2))`,

so the current rigorous moving-cutoff source-compression frontier is

`m/N^2 -> infinity  =>  beta_(N+1)(m) -> 0`.

This supersedes the earlier sufficient scales `m/P_N -> infinity`, `m/N^3 -> infinity`, and `m/N^(5/2) -> infinity`. The improvement is source-native and condition-number free. NB-303 also removes the logarithmic Cesàro loss and the pairwise phase-remainder bottleneck of NB-302; it does not claim that the quadratic scale is necessary or optimal.

In first-free notation with old section `V_(n-1)`, set

`epsilon_LS(m,n)^2=min(1, 10(n-1)^2/m + 20(n-1)^4/(3m^2))`.

For a finite off-critical packet `Z`, the exact NB-299 factorization gives

`||Xi_(m,n,Z)|| <= ||K_(n-1,Z)|| (m^(-delta_Z)+epsilon_LS(m,n))^2/[1-epsilon_LS(m,n)^2]`

whenever `epsilon_LS<1`. Consequently,

`m/(n-1)^2 -> infinity` and `delta_Z log m -> infinity`

force `||Xi||/||K|| -> 0`, even while the section depth moves. Persistent normalized destination occupation therefore cannot be rescued merely by generic source overlap throughout the super-quadratic dilation regime.

The reusable frontier is now sharper. NB-300 removed the global-period obstruction, NB-301 priced source coordinates polynomially, NB-302 exposed the pairwise `N^2` time scale, and NB-303 converts that same arithmetic scale into a direct Farey-frequency frame that controls the full shell sequence. Any surviving projected-dilation mechanism must now live in the near/sub-quadratic window `m=O(N^2)`, keep `delta_Z log m` weak, or use destination-side structure that generic source compression does not see.

This still does **not** control `Xi` relative to the unresolved future-tail Gram `E`, prove decay of the original Nyman distance, remove moving-packet sample conditioning, or certify occupation of the relevant Ford target. Those destination/target-aware questions, rather than generic large-dilation source overlap, are the durable remaining bottleneck.