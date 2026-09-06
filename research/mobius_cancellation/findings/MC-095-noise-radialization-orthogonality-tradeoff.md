# MC-095 — Noise radialization separates cheap endpoint reconstruction from full Walsh orthogonality

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The prime-symmetric-difference deformation of `MC-091`--`MC-094` is exactly a Boolean-noise radialization of the product-fiber Walsh expansion from `MC-092`. This makes precise a structural tradeoff that the previous findings left implicit:

- the full square-free-kernel Walsh basis has exact second-moment orthogonality, but a generic estimate of one distinguished all-minus point from that `L^2` information alone loses an entire polynomial power;
- the one-parameter Hamming deformation collapses the full Walsh basis to only `O(log N/log log N)` degree shells, so endpoint reconstruction is subpolynomial, but every statistic built only from the deformation values has already forgotten all orthogonality **within** a fixed `omega(a)` shell.

Thus the critical matched-control RMS from the product-fiber Walsh representation and the cheap endpoint interpolation from `MC-093`--`MC-094` cannot simply be combined as two independent free gains. A surviving route must prove new arithmetic cancellation inside the degree shells, or find an intermediate source-forced quotient that retains more than degree while still admitting cheap reconstruction.

No improved Mertens bound is proved.

## 1. Exact Boolean-noise representation

Use the product-fiber coefficient from `MC-092`

\[
W_N(a)
:=
\sum_{\substack{b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
R_N(a,b)
 z\!\left(\frac{N^2}{ab^2}\right),
\tag{1}
\]

for square-free `a`. Then its deformation identity is

\[
\mathcal Q_N(t)
=
\sum_{a\ \mathrm{squarefree}}
\mu(a)t^{\omega(a)}W_N(a).
\tag{2}
\]

Let the Boolean cube have one sign coordinate `xi_p in {-1,+1}` for every prime that can occur, and write

\[
\chi_a(\xi):=\prod_{p\mid a}\xi_p,
\qquad
F_N(\xi):=\sum_a W_N(a)\chi_a(\xi).
\tag{3}
\]

The characters `chi_a` are the standard Walsh basis. If `T_t` is the standard Boolean noise operator, characterized on Walsh characters by

\[
T_t\chi_a=t^{\omega(a)}\chi_a,
\tag{4}
\]

then at the all-minus vertex `-\mathbf 1`, where `chi_a(-\mathbf 1)=(-1)^{\omega(a)}=mu(a)`, one has the exact identity

\[
\boxed{
\mathcal Q_N(t)=(T_tF_N)(-\mathbf 1).
}
\tag{5}
\]

For real `0<=t<=1`, this is the same biased-random-multiplicative expectation already derived in `MC-093`; `(5)` identifies its standard Boolean-harmonic form. The identity itself is classical noise-operator algebra once the source-specific product-fiber quotient is known.

Walsh Parseval gives

\[
\|F_N\|_2^2=\sum_a |W_N(a)|^2.
\tag{6}
\]

The elementary product-fiber bound from `MC-092`,

\[
|W_N(a)|
\le
\frac{N}{2\sqrt a}2^{\omega(a)},
\tag{7}
\]

therefore gives

\[
\boxed{
\|F_N\|_2
=O\!\left(N(\log N)^2\right).
}
\tag{8}
\]

This is the same critical square-scale **power** supplied by the matched random-multiplicative second moment. It does not control the distinguished all-minus evaluation.

## 2. Generic Walsh `L^2` control alone spends a full power at a fixed bias

For fixed `0<r<1`, Cauchy--Schwarz applied directly to `(2)` gives

\[
|\mathcal Q_N(r)|
\le
\left(
\sum_{\substack{a\le N^2\\a\ \mathrm{squarefree}}}
r^{2\omega(a)}
\right)^{1/2}
\left(
\sum_a |W_N(a)|^2
\right)^{1/2}.
\tag{9}
\]

The first factor is the exact norm of the evaluation functional on the ambient square-free Walsh coefficient space after the noise multiplier. The classical Selberg--Delange theorem, applied to the nonnegative multiplicative function

\[
a\mapsto\mu(a)^2r^{2\omega(a)},
\]

gives for fixed `r`

\[
\sum_{a\le X}\mu(a)^2r^{2\omega(a)}
=
C_r X(\log X)^{r^2-1}(1+o(1)),
\qquad C_r>0.
\tag{10}
\]

Hence at `X=N^2`,

\[
\left(
\sum_{a\le N^2}\mu(a)^2r^{2\omega(a)}
\right)^{1/2}
=
N(\log N)^{(r^2-1)/2+o(1)}
=
N^{1+o(1)}.
\tag{11}
\]

Combining `(8)` and `(11)` yields only the generic estimate

\[
|\mathcal Q_N(r)|
\le
N^{2+o(1)}.
\tag{12}
\]

The point is not that the actual source vector `W_N` must saturate `(9)`. It need not. The exact statement is a **sufficiency obstruction**: Walsh Parseval at the matched-control scale plus the standard noise multiplier, with no further arithmetic information about `W_N`, does not force a critical-power pointwise value. The evaluation functional itself has polynomial norm on the ambient coefficient class. Any improvement for the source vector must exploit additional structure or cancellation beyond its `L^2` size.

This is compatible with `MC-093`--`MC-094`: those findings do not estimate one noisy evaluation from full Walsh `L^2`; they first collapse the source to a low-degree one-variable polynomial and then reconstruct one endpoint from other values of that **same collapsed polynomial**.

## 3. The one-parameter deformation remembers only degree-shell sums

Define

\[
C_{k,N}
:=
\sum_{\substack{a\ \mathrm{squarefree}\\\omega(a)=k}}W_N(a).
\tag{13}
\]

Then exactly

\[
\boxed{
\mathcal Q_N(t)
=
\sum_{k=0}^{K_N}(-t)^k C_{k,N},
}
\tag{14}
\]

where `K_N=O(log N/log log N)` as in `MC-093`--`MC-094`.

Equation `(14)` is an information quotient: **all values of the entire one-parameter deformation, for all real or complex `t`, depend on the product-fiber vector `W_N(a)` only through the `K_N+1` shell sums `C_{k,N}`.** In particular, a second moment over Chebyshev bias nodes as suggested in `MC-094` is a second moment of the degree-shell polynomial. It cannot automatically import the full Walsh orthogonality `(6)`, because that orthogonality distinguishes different square-free kernels with the same `omega(a)` while `(14)` has already identified them.

There is an exact finite Parseval formula that exposes the quotient cleanly. Fix `0<r<1`, put `L_N=K_N+1`, and let

\[
\theta_j:=\frac{2\pi j}{L_N},
\qquad j=0,\dots,L_N-1.
\tag{15}
\]

Discrete Fourier orthogonality gives

\[
\boxed{
\frac1{L_N}
\sum_{j=0}^{L_N-1}
|\mathcal Q_N(re^{i\theta_j})|^2
=
\sum_{k=0}^{K_N}r^{2k}|C_{k,N}|^2.
}
\tag{16}
\]

Conversely, Cauchy--Schwarz on the degree shells gives

\[
|\mathcal Q_N(1)|
\le
\left(
\sum_{k=0}^{K_N}r^{2k}|C_{k,N}|^2
\right)^{1/2}
\left(
\sum_{k=0}^{K_N}r^{-2k}
\right)^{1/2}.
\tag{17}
\]

For fixed `r`, the second factor is

\[
\exp(O_r(K_N))
=
N^{o_r(1)}.
\tag{18}
\]

Thus a strict-power `L^2` estimate for the **degree-shell sums** transfers to the Möbius endpoint with subpolynomial loss, just as the real Chebyshev-node estimate of `MC-094` does by a different sampling geometry. But `(16)` makes the missing arithmetic theorem explicit: one must control the coherent shell sums `C_{k,N}`. Full product-fiber Walsh variance does not do that after radialization.

The complex samples in `(16)` are an algebraic Fourier device, not biased probability ensembles; no probabilistic interpretation is claimed for complex `t`.

## 4. Exact full-fiber orthogonality cannot be compressed to the shell-sized sample family for free

The same distinction has a finite-dimensional rank formulation. Let `A` be any finite set of distinct square-free kernels and consider their Walsh characters `chi_a`. Suppose a weighted sample set `xi^(1),...,xi^(L)` were to reproduce exact Walsh Parseval for **every** coefficient vector `(c_a)_{a in A}`:

\[
\sum_{j=1}^L w_j
\left|
\sum_{a\in A}c_a\chi_a(\xi^{(j)})
\right|^2
=
\sum_{a\in A}|c_a|^2.
\tag{19}
\]

Writing `V_{j,a}=sqrt(w_j) chi_a(xi^(j))`, equation `(19)` is `V^*V=I_|A|`. Therefore

\[
\boxed{L\ge |A|.}
\tag{20}
\]

This is only rank. It is nevertheless enough to rule out a free exact replacement of full product-fiber Walsh orthogonality by the `K_N+1` samples that suffice after degree collapse. The latter work precisely because the map `W_N(a) -> C_{omega(a),N}` has already reduced the coefficient space to at most `K_N+1` dimensions.

The rank statement must not be overstated. Small-bias probability spaces of Naor--Naor give much smaller finite ensembles whose individual nontrivial parity expectations are approximately zero, and more general pseudorandom constructions can approximate selected tests. Such results do not contradict `(20)`: when `L<|A|`, the sampling Gram matrix has a nontrivial kernel and cannot be a uniformly lower-bounded isometry on the entire `|A|`-dimensional coefficient space. Approximate or source-vector-specific compression may still be useful, but then the required coefficient structure is additional mathematical input rather than a consequence of Walsh orthogonality alone.

## 5. Prior art and novelty boundary

Walsh--Fourier expansion, Parseval, the Boolean noise operator `T_rho`, its degree multiplier `rho^{|S|}`, and hypercontractive methods are standard; a modern reference is Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014, DOI `10.1017/CBO9781139814782`.

The small-bias boundary is classical: Joseph Naor and Moni Naor, *Small-Bias Probability Spaces: Efficient Constructions and Applications*, SIAM Journal on Computing 22 (1993), no. 4, 838--856, DOI `10.1137/0222053`, constructs polynomial-size distributions with approximately unbiased parities.

The asymptotic `(10)` is a standard Selberg--Delange specialization. The existing source `MC-S14` supplies the needed general partial-sum theorem from prime averages; here `f(p)=r^2` and `f(p^nu)=0` for `nu>=2`, giving exponent `r^2-1` and a positive Euler-product leading constant.

Discrete Fourier Parseval on the degree variable and the rank argument `(19)`--`(20)` are elementary finite harmonic analysis and linear algebra. **No novelty claim is made for any of these ingredients.** The durable line-specific result is their exact composition with the source-forced product-fiber/Hamming quotient from `MC-092`--`MC-094`, which identifies where the two previously attractive second-moment mechanisms cease to be interchangeable.

## 6. Boundaries and decisive continuation

This finding does not show that Boolean harmonic analysis, hypercontractivity, small-bias sampling, large-sieve methods, or another orthogonality argument cannot help. It rules out only the inference that the already available full Walsh `L^2` normalization can be passed through the one-parameter deformation and then combined with cheap interpolation **without proving another arithmetic estimate**.

Nor does the ambient evaluation norm in `(11)` prove that the actual Huxley--Watt coefficient vector is extremal. A source-specific theorem may place `W_N` in a much smaller or more regular class. Such a theorem is exactly the kind of new information the line is seeking.

The decisive continuation is now one of two forms:

1. prove a strict-power estimate for the shell vector, for example
   \[
   \sum_{k=0}^{K_N}r^{2k}|C_{k,N}|^2
   \le N^{2\alpha+o(1)}
   \]
   with `alpha` below the old square-scale exponent, from hypotheses independently weaker than the desired Mertens improvement; or
2. construct an intermediate source-forced family that keeps enough square-free-kernel information for a genuine orthogonality theorem while having an endpoint reconstruction condition number only `N^{o(1)}`.

A route is killed if its only second-moment input is `(6)`/`(8)` and its only transfer step is radial Hamming interpolation, because `(14)` shows that the transfer first quotients away the fiber coordinates on which `(6)` is diagonal. A surviving route must control the within-shell coherence or avoid that quotient.

## Consequence for the research line

`MC-092` identified the correct deterministic product-fiber parity target; `MC-093` and `MC-094` showed that the Hamming deformation has cheap fixed-gap endpoint reconstruction, even from a sublogarithmic sampled family. `MC-095` separates those facts sharply: **the low-dimensional deformation and the high-dimensional Walsh variance live on different information layers**.

This removes a tempting but invalid shortcut from the live route. The remaining opportunity is more specific: obtain arithmetic cancellation after grouping by `omega(a)`, or design a different source-forced quotient whose orthogonality and reconstruction properties coexist rather than being supplied by two incompatible representations.