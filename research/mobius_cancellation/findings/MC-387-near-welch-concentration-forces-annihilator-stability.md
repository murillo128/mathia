# MC-387 — Near-Welch concentration forces annihilator stability

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `STABILITY-THEOREM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Let

\[
W=\mathbf F_2^d,
\qquad H=|W|,
\]

and let `g:W->R` be the normalized positive-definite Cayley kernel of `MC-386`:

\[
g(0)=1,
\qquad
G_{I,J}=g(I+J)\succeq0,
\qquad
\operatorname{rank}G\le R.
\tag{1}
\]

Write the finite Bochner/Fourier representation

\[
g(x)=\sum_{\xi\in\widehat W}p(\xi)\,\xi(x),
\qquad p(\xi)\ge0,
\qquad \sum_\xi p(\xi)=1,
\tag{2}
\]

and let `S=supp(p)`, `r=|S|<=R`. Suppose a sequence of such kernels satisfies, for parameters `alpha,beta,gamma -> 0`,

\[
\sum_{x\in W}|g(x)|^2\le (1+\alpha)\frac HR,
\tag{3}
\]

and there is a set `A subset W` such that

\[
|A|\le (1+\beta)\frac HR,
\qquad
\sum_{x\notin A}|g(x)|^2\le \gamma\frac HR.
\tag{4}
\]

Thus the frame is nearly Welch-minimal and almost all of its physical `L^2` energy is concentrated on essentially the smallest support scale allowed by `MC-386`.

Then the abstract near-extremizer is rigid. More precisely, as `alpha,beta,gamma -> 0` there exists a coset

\[
C=\xi_0+L\subset\widehat W
\]

of a subgroup `L<=\widehat W` such that

\[
|S\triangle C|=o(R),
\qquad
|L|=(1+o(1))R,
\tag{5}
\]

and, if `u_C` is the uniform probability measure on `C`,

\[
\|p-u_C\|_2=o(R^{-1/2}).
\tag{6}
\]

Let

\[
K=L^\perp\le W.
\]

The inverse Fourier transform of `u_C` is exactly

\[
h(x)=\xi_0(x)1_K(x).
\tag{7}
\]

Consequently

\[
\sum_{x\in W}|g(x)-h(x)|^2=o(H/R),
\tag{8}
\]

and the physical concentration set itself is asymptotically an annihilator subgroup:

\[
|A\triangle K|=o(H/R).
\tag{9}
\]

Hence the subgroup/annihilator extremizer in `MC-386` is not merely one sharp example. **Any** PSD Cayley frame that simultaneously nearly saturates the Welch energy floor and concentrates that energy on the minimal `H/R` physical scale must approach the same coset/annihilator geometry.

The theorem closes the finite-harmonic stability question in `CLUE-cayley-welch-near-extremizer-geometry`. The remaining live question is arithmetic: can the actual quadratic-character source frame realize, or even approach, this near-coset Fourier support and annihilator concentration without violating its conductor/source-prime structure?

No estimate for `M(x)` follows.

## 1. Positive definiteness turns the frame into a probability measure

Because `W` is a finite abelian group and `G` is a positive-semidefinite Cayley matrix, its characters diagonalize `G` with nonnegative eigenvalues. Normalizing by `g(0)=1` gives `(2)`, with `p` a probability measure on `widehat W`.

With the unnormalized character transform used in `(2)`, Parseval gives

\[
\sum_{x\in W}|g(x)|^2
=H\sum_{\xi\in\widehat W}p(\xi)^2
=H\|p\|_2^2.
\tag{10}
\]

Since `p` is supported on `r` points,

\[
\|p\|_2^2\ge \frac1r\ge\frac1R.
\tag{11}
\]

This is exactly the Welch floor from `MC-386` in Fourier coordinates. Combining `(3)` and `(11)` yields

\[
\frac1r\le\|p\|_2^2\le\frac{1+\alpha}{R},
\qquad
r\ge\frac{R}{1+\alpha}.
\tag{12}
\]

Thus `r/R -> 1`: a near-Welch kernel must use almost all of its allowed Fourier rank.

Let `u_S=1_S/r`. Since `sum_S p=1`,

\[
\|p-u_S\|_2^2
=\|p\|_2^2-\frac1r
\le\frac{\alpha}{R}.
\tag{13}
\]

So near equality in the trace/rank bound already forces the nonzero Fourier eigenvalues to be nearly uniform on their support.

## 2. Minimal physical concentration forces near equality in Young

From the lower Welch bound and `(4)`,

\[
\sum_{x\in A}|g(x)|^2
\ge (1-\gamma)\frac HR.
\tag{14}
\]

Cauchy--Schwarz on `A` gives

\[
\sum_x|g(x)|^4
\ge
\frac{\left(\sum_{x\in A}|g(x)|^2\right)^2}{|A|}
\ge
\frac{(1-\gamma)^2}{1+\beta}\frac HR.
\tag{15}
\]

Because `W=F_2^d`, every character is real and inversion equals negation. The Fourier coefficients of `g^2=|g|^2` are therefore the convolution `p*p`. A second application of Parseval gives

\[
\sum_x|g(x)|^4=H\|p*p\|_2^2.
\tag{16}
\]

Hence

\[
\|p*p\|_2^2
\ge
\frac{(1-\gamma)^2}{1+\beta}\frac1R.
\tag{17}
\]

On the other hand, because `p` is a probability measure, Young's inequality gives

\[
\|p*p\|_2\le\|p\|_2.
\tag{18}
\]

Equations `(3)`, `(10)` and `(17)` therefore imply

\[
\frac{\|p*p\|_2^2}{\|p\|_2^2}
\ge
\frac{(1-\gamma)^2}{(1+\beta)(1+\alpha)}
=1-o(1).
\tag{19}
\]

So near-minimal physical concentration converts directly into **near equality in the `l^1*l^2 -> l^2` Young contraction** for the Fourier probability measure.

## 3. The Fourier support has near-maximal additive energy

The weighted measure `p` is already close to the uniform measure `u_S` by `(13)`. Since both have `l^1` norm one,

\[
\|p*p-u_S*u_S\|_2
\le
\|(p-u_S)*p\|_2+\|u_S*(p-u_S)\|_2
\le2\|p-u_S\|_2
\le2\sqrt{\alpha/R}.
\tag{20}
\]

Combining `(17)` and `(20)` gives the explicit lower bound

\[
\|u_S*u_S\|_2
\ge
\frac1{\sqrt R}
\left(
\frac{1-\gamma}{\sqrt{1+\beta}}-2\sqrt\alpha
\right)_+.
\tag{21}
\]

If `E(S)` denotes additive energy,

\[
E(S)=\#\{(a,b,c,d)\in S^4:a+b=c+d\},
\]

then

\[
\|u_S*u_S\|_2^2=\frac{E(S)}{r^4}.
\tag{22}
\]

Using `r/R>=1/(1+alpha)` from `(12)`, `(21)` yields

\[
\boxed{
\frac{E(S)}{r^3}
\ge
\frac1{1+\alpha}
\left(
\frac{1-\gamma}{\sqrt{1+\beta}}-2\sqrt\alpha
\right)_+^2.
}
\tag{23}
\]

The right-hand side tends to one. Thus the Fourier support has asymptotically maximal additive energy:

\[
E(S)=(1-o(1))r^3.
\tag{24}
\]

This is the structural bridge missing from `MC-386`: physical concentration of the Cayley kernel forces additive closure of its Fourier support.

## 4. Near-maximal additive energy forces a coset

Write

\[
r_S(t)=\#\{(a,b)\in S^2:a+b=t\}.
\]

Then

\[
\sum_t r_S(t)=r^2,
\qquad
\sum_t r_S(t)^2=E(S).
\tag{25}
\]

If `E(S)>=(1-delta)r^3`, then

\[
\sum_t r_S(t)(r-r_S(t))
=r^3-E(S)
\le\delta r^3.
\tag{26}
\]

Fix a small `eta>0` and call a pair `(a,b)` good when

\[
r_S(a+b)\ge(1-\eta)r.
\]

Every bad pair contributes more than `eta r` to the left side of `(26)`, so at most `(delta/eta)r^2` pairs are bad. Meanwhile the restricted sumset of good pairs contains at most

\[
\frac{r}{1-\eta}
\tag{27}
\]

sums, because each represented sum has at least `(1-eta)r` representations and there are only `r^2` pairs in total.

Xuancheng Shao's Lemma 4.4 in *Additive energies of subsets of discrete cubes* is precisely the robust finite-group statement needed here: an almost-complete pair graph on two equal finite sets whose restricted sumset has size at most `(1+epsilon)` times the set size forces the set to be close to a coset of a subgroup. Applying that lemma to the good-pair graph, with `eta` chosen in terms of the target structural error and then `delta` sufficiently small, gives a coset

\[
C=\xi_0+L
\]

such that

\[
|S\setminus C|=o(r),
\qquad
|C\setminus S|=o(r).
\tag{28}
\]

Together with `r=(1+o(1))R`, this proves `(5)`.

Because `S` and `C` differ by `o(r)` points and `|C|=(1+o(1))r`, their uniform measures obey

\[
\|u_S-u_C\|_2=o(r^{-1/2}).
\tag{29}
\]

Combining `(13)` and `(29)` proves `(6)`.

The use of Shao's lemma is qualitative here: it certifies `o(1)` stability but does not supply a useful explicit modulus `delta(epsilon)` for this application. The exact quantitative bridge up to additive-energy near-maximality is `(23)`.

## 5. Fourier coset rigidity returns as annihilator rigidity

For the uniform probability measure on `C=xi_0+L`, character orthogonality gives

\[
\sum_{\xi\in C}\frac1{|L|}\xi(x)
=\xi_0(x)1_{L^\perp}(x).
\tag{30}
\]

Set `K=L^perp`. Parseval and `(6)` imply

\[
\sum_x|g(x)-\xi_0(x)1_K(x)|^2
=H\|p-u_C\|_2^2
=o(H/R),
\tag{31}
\]

which is `(8)`.

It remains to compare the arbitrary concentration set `A` with `K`. On `K`, the model kernel `h=xi_0 1_K` has unit modulus. Therefore

\[
|K\setminus A|
\le
2\sum_x|g(x)-h(x)|^2
+2\sum_{x\notin A}|g(x)|^2
=o(H/R).
\tag{32}
\]

Also

\[
|K|=\frac{H}{|L|}=(1+o(1))\frac HR,
\tag{33}
\]

while `|A|<=(1+beta)H/R`. Hence

\[
|A\setminus K|
=|A|-|K|+|K\setminus A|
=o(H/R).
\tag{34}
\]

Equations `(32)` and `(34)` prove `(9)`.

Thus the finite harmonic problem has a sharp stability answer: near extremizers cannot spread their exceptional energy over an arbitrary thin set. They must asymptotically look like the subgroup/annihilator model already exhibited by exact equality.

## 6. What remains arithmetic

The conclusion is deliberately abstract. It says that a source frame capable of evading the `MC-386` exception-energy barrier at essentially optimal cardinality must have **dual Fourier mass close to a subgroup coset**, while its large physical correlations live close to the corresponding annihilator subgroup.

That reduces the endpoint escape to a concrete arithmetic question rather than a generic frame question. For the actual source rows built from quadratic characters, one must now determine whether such a near-subgroup pattern is compatible with:

- multiplication of primitive quadratic characters;
- conductor reduction of products;
- reuse of lower-prime source factors;
- the exact map from source subsets to primitive conductors;
- the endpoint rank/source-cost constraints already established in `MC-374`--`MC-386`.

If those arithmetic rules forbid a near-coset support, the abstract sharpness example ceases to be an admissible endpoint control. If they permit one, the stability theorem instead shows that the `H/R` exceptional scale is not only abstractly sharp but structurally reachable by the arithmetic source family.

Neither conclusion is proved here.

## Prior art and novelty boundary

The ingredients are established mathematics.

- Welch/frame-potential lower bounds and the exact annihilator-subgroup extremizer were already audited in `MC-386` against L. R. Welch (1974), Benedetto--Fickus (2003), and finite-group uncertainty literature.
- Aline Bonami and Saifallah Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, Acta Scientiarum Mathematicarum **79** (2013), 507--528, DOI `10.1007/BF03651331`, studies equality cases of finite-group uncertainty principles and records the classical subgroup/coset extremal phenomenon in the divisible-support regime.
- Xuancheng Shao, *Additive energies of subsets of discrete cubes*, Proceedings of the Royal Society of Edinburgh Section A: Mathematics **156** (2026), 944--965, DOI `10.1017/prm.2024.126`, published online 18 November 2024, treats near-maximal additive energy via robust additive-combinatorial inverse machinery. Lemma 4.4 gives the generic abelian-group restricted-sumset-to-coset stability statement used above.
- K. Aldahleh, A. Iosevich, J. Iosevich, J. Jaimangal, A. Mayeli and S. Pack, *Additive energy, uncertainty principle and signal recovery mechanisms*, arXiv:2504.14702 (2025), explicitly strengthens finite-group uncertainty bounds using additive energy.
- Ivan Bortnovskyi et al., *Refined additive uncertainty principle*, arXiv:2510.26664 (2025), adds correction terms measuring departure from highly structured extremal supports such as subgroup cosets. This is very close conceptual prior art for using additive structure to quantify non-extremality of Fourier support.

No novelty is claimed for near-equality methods, additive energy, Balog--Szemeredi--Gowers/Kneser stability, uncertainty extremizers, or subgroup Fourier duality. The line-specific contribution is the explicit composition `(13)`--`(23)` and its consequence for the exact `MC-386` Cayley source frame: **near-Welch energy plus near-minimal physical concentration forces the source exception geometry itself to approach an annihilator subgroup**. The literature search found the component mechanisms and closely adjacent refined uncertainty principles, but not this exact source-frame statement as a standalone theorem.

## Boundaries

- This is a finite-harmonic stability theorem, not an arithmetic exclusion theorem.
- The `o(1)` coset-stability conclusion is qualitative because the invoked robust sumset lemma is used qualitatively; `(23)` is the explicit quantitative part.
- Positive definiteness and the Cayley structure are essential. Arbitrary low-rank Gram families need not admit the probability-measure/convolution reduction.
- The elementary `2`-group hypothesis is used to identify the Fourier transform of `|g|^2` directly with `p*p`. An analogous statement for general finite abelian groups would use `p*\widetilde p` and needs separate bookkeeping.
- The theorem assumes both near-Welch energy and near-minimal physical concentration. Either hypothesis alone is insufficient.
- The result does not show that primitive quadratic source characters satisfy the near-extremal hypotheses, nor that they cannot.
- No statement about zeta zeros, RH, or the true order of `M(x)` is made.
