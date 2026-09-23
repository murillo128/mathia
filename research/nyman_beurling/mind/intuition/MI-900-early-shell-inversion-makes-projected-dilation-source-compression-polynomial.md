# MI-900 — Early-shell inversion makes projected-dilation source compression polynomial

**Evidence level:** proved source-compression bounds from [NB-300](../../findings/NB-300-reciprocal-cell-periodicity-gives-explicit-moving-cutoff-source-compression.md), [NB-301](../../findings/NB-301-early-shell-mobius-inversion-gives-cubic-moving-cutoff-source-compression.md), and the stronger [NB-302](../../findings/NB-302-pairwise-shell-periodicity-lowers-moving-cutoff-source-compression-to-five-halves.md), combined with the exact projected-dilation factorization of NB-297--NB-299.

The large-dilation obstruction is not tied to the exponential reciprocal-cell period. For `U_N=span{g_2,...,g_N}`, NB-301 uses the first `N` harmonic shells and finite Möbius inversion to recover every coefficient of `u=sum a_jg_j`, giving

`sum_(j=2)^N |a_j| <= sqrt(6) N^(3/2)||u||_2`.

That already reduced the NB-300 lcm-scale condition to the cubic sufficient condition `m/N^3 -> infinity`. NB-302 improves the source-overlap estimate by using the quadratic structure before taking absolute values: each product of reciprocal-shell sawteeth `r_i(k)r_j(k)` has period `lcm(i,j)<=ij<=N^2`, even though the complete shell vector can have exponential common period.

Writing `H_N=sum_(q<=N)1/q`, NB-302 proves the uniform tail bound

`||1_(0,1/m] u||_2^2 <= B_(N,m)||u||_2^2`,

with

`B_(N,m)=N^2(9+H_N^3/2)/m + 6N^5/[m(m+1)]`.

Hence the projected-dilation overlap satisfies

`beta_(N+1)(m)^2 <= min(1,B_(N,m))`,

so the current rigorous moving-cutoff source-compression frontier is

`m/N^(5/2) -> infinity  =>  beta_(N+1)(m) -> 0`.

This supersedes the earlier sufficient scales `m/P_N -> infinity`, with `P_N=lcm(2,...,N)`, and `m/N^3 -> infinity`. The improvement is source-native: it comes from exact pairwise residue correlations plus early-shell Möbius control, not from a source Gram condition number.

In first-free notation with old section `V_(n-1)`, let

`epsilon_pair(m,n)=min(1,sqrt(B_(n-1,m)))`.

For a finite off-critical packet `Z`, the exact NB-299 factorization gives

`||Xi_(m,n,Z)|| <= ||K_(n-1,Z)|| (m^(-delta_Z)+epsilon_pair(m,n))^2/[1-epsilon_pair(m,n)^2]`

whenever `epsilon_pair<1`. Consequently,

`m/(n-1)^(5/2) -> infinity` and `delta_Z log m -> infinity`

force `||Xi||/||K|| -> 0`, even while the section depth moves. Persistent normalized destination occupation therefore cannot be rescued merely by source overlap throughout the super-five-halves dilation regime.

The exponent `5/2` is a sufficient exponent, not an optimality claim. The present bottleneck is the phase-error term `6N^5/m^2`, obtained by taking absolute values of pairwise periodic tail remainders. Cancellation in that remainder matrix, or a target-aware estimate, could lower the threshold further. The result still does **not** control `Xi` relative to the unresolved future-tail Gram `E`, prove decay of the original Nyman distance, or remove moving-packet sample-conditioning/target-occupation issues.

The reusable picture is now: NB-300 removes the global-period obstruction, NB-301 prices source coordinates polynomially, and NB-302 exploits pairwise periodicity to push the uniform source-compression threshold to `N^(5/2)`. Any surviving projected-dilation mechanism must live at or below that scale, keep `delta_Z log m` weak, or exploit genuinely destination-side structure rather than generic source overlap.