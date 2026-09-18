# MC-377 — Smooth-subspace prime frame forces superpolynomial common source cost

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `DECISIVE-NEGATIVE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint partition and lower-prime source-package setup of `MC-296`, `MC-371`, `MC-374`, and `MC-375`. Let

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad R\to\infty,
\]

be the prime shell split into its `R` nonempty defect cells, with independent endpoint generators `\lambda_1,\ldots,\lambda_R`. Choose arbitrary fixed lower-prime product representatives `V_i` for those generators and define

\[
U:=\bigcup_{i=1}^R V_i,
\qquad
P:=\prod_{p\in U}p.
\tag{1}
\]

Then an exact endpoint realization cannot have polynomial common source cost. More precisely,

\[
\boxed{
\frac{\log P}{\log y}\longrightarrow\infty.
}
\tag{2}
\]

Equivalently, for every fixed `A>0`, all sufficiently large exact endpoints satisfy

\[
\boxed{P>y^A.}
\tag{3}
\]

This strictly strengthens the quartic lower floor of `MC-371`. In particular, the quartic-saturation regime

\[
P=y^{4+o(1)}
\]

studied conditionally in `MC-372`--`MC-376` is impossible for an actual exact endpoint source package. The same is true of every other fixed-power common-radical regime.

The mechanism is not another fixed-subquadratic Burgess estimate. If `P<=y^A`, only `O_A(1)` source primes can be larger than a suitably chosen fixed power `y^theta`. Killing the incidence columns of those finitely many rough primes leaves a subspace of endpoint modes of dimension `R-O_A(1)`. Every package character in that subspace, and every pairwise product appearing in its Gram matrix, then has a **smooth ambient modulus** bounded by `P`. Cochrane--Granville--Zheng's 2026 incomplete-character theorem gives a fixed power saving for the ordinary character sums inside Schlage-Puchta's Selberg-sieve transfer. Bombieri's frame inequality consequently gives a bounded prime-frame row scale, whereas the exact endpoint partition forces largest frame eigenvalue at least `2^{R-O(1)}/R`. These are incompatible.

No estimate for `M(x)` follows.

## 1. A polynomial radical has only finitely many rough source coordinates

Assume for contradiction that along an infinite sequence of exact endpoints there is a fixed constant `A>0` with

\[
P\le y^A.
\tag{4}
\]

There is no loss in increasing `A` so that `A>1`. Set, for definiteness,

\[
\theta:=\frac1{4A}.
\tag{5}
\]

Call a source prime rough when `p>y^theta`. Since every such prime contributes more than `theta log y` to `log P`,

\[
\#\{p\in U:p>y^\theta\}
\le \frac{\log P}{\theta\log y}
\le \frac A\theta
=4A^2.
\tag{6}
\]

Thus only a bounded number of source coordinates can obstruct smooth-modulus estimates.

For each `p\in U`, let

\[
c_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbb F_2^R
\tag{7}
\]

be its source-incidence column. For `I\in\mathbb F_2^R`, write

\[
V_I:=\mathop\triangle_{i:I_i=1}V_i,
\qquad
\chi_I:=\prod_{p\in V_I}\left(\frac{\cdot}{p}\right).
\tag{8}
\]

Then

\[
p\in V_I
\iff
\langle I,c_p\rangle=1.
\tag{9}
\]

We also need to remove the fixed finite exceptional-prime set in the smooth-modulus theorem. Choose below fixed parameters `delta,epsilon`; let `\mathcal M=\mathcal M(\delta)` be the explicitly determinable integer in Cochrane--Granville--Zheng Corollary 2. Define

\[
E_y:=\{p\in U:p>y^\theta\}
\cup
\{p\in U:p\mid\mathcal M\}.
\tag{10}
\]

By `(6)` and fixedness of `\mathcal M`,

\[
|E_y|=O_A(1).
\tag{11}
\]

Now take the common kernel

\[
W:=\{I\in\mathbb F_2^R:
\langle I,c_p\rangle=0\text{ for every }p\in E_y\}.
\tag{12}
\]

Its codimension is at most `|E_y|`, so

\[
\boxed{
\dim W\ge R-O_A(1),
\qquad
H:=|W|\ge2^{R-O_A(1)}.
}
\tag{13}
\]

For every `I\in W`, `(9)` gives

\[
V_I\cap E_y=\varnothing.
\tag{14}
\]

Hence every prime factor of the package conductor of `\chi_I` is at most `y^theta` and is coprime to `\mathcal M`. The same remains true for the ambient lcm modulus of any pair `\chi_I,\chi_J` with `I,J\in W`.

The package characters indexed by `W` are distinct. Indeed, if `\chi_I=\chi_J` as source characters, their quotient is trivial, so its restriction to the shell is trivial. But the restriction is the endpoint mode `\lambda_{I+J}`; independence of `\lambda_1,\ldots,\lambda_R` forces `I=J`. In particular every off-diagonal pair product is nonprincipal.

## 2. Smooth incomplete sums give a power-saving Selberg off-diagonal

We now revisit the proof of Schlage-Puchta's prime Halasz--Montgomery inequality rather than using its worst-case varying-modulus clause.

Let `N=2y`. Choose fixed constants

\[
\theta<\delta<\frac1A
\tag{15}
\]

and then fixed `epsilon>0` so small that

\[
A\delta(1+\epsilon)<1.
\tag{16}
\]

Cochrane--Granville--Zheng Corollary 2 (`MC-S46`) gives a fixed `eta=eta(delta,epsilon)>0` such that a nonprincipal character modulo a modulus `q\in\mathcal N(q^\delta)`, coprime to `\mathcal M`, has

\[
\left|\sum_{n\in J}\chi(n)\right|
\ll |J|^{1-\eta}
\tag{17}
\]

for every interval `J` in their admissible range

\[
q\ge |J|\ge q^{\delta(1+\epsilon)}.
\tag{18}
\]

Choose a fixed `b>0` sufficiently small that

\[
\delta(1-2b)>\theta,
\qquad
A\delta(1+\epsilon)<1-2b,
\qquad
2b<\eta/2.
\tag{19}
\]

Let

\[
B:=y^b
\tag{20}
\]

be the Selberg-sieve cutoff in Schlage-Puchta Lemma 8, let `g` be the corresponding sieve function, and put

\[
f=(1*g)^2.
\tag{21}
\]

For an off-diagonal pair `I\ne J` in `W`, the weighted inner product in Schlage-Puchta's Bombieri argument is a sum

\[
S_{I,J}:=
\sum_{n\le N}f(n)\psi_{I,J}(n),
\tag{22}
\]

where `\psi_{I,J}` is the nonprincipal product character modulo

\[
q_{I,J}:=[q_I,q_J]\mid P.
\tag{23}
\]

Its ambient modulus may contain local principal factors coming from overlap between `V_I` and `V_J`; this is harmless because Corollary 2 is stated for nonprincipal characters modulo `q`, not only primitive ones. By `(14)`, every prime factor of `q_{I,J}` is at most `y^theta` and `q_{I,J}` is coprime to `\mathcal M`.

Expand the Selberg weight exactly as in Schlage-Puchta Proposition 9:

\[
S_{I,J}
=
\sum_{d_1,d_2\le B}
 g(d_1)g(d_2)\,
 \psi_{I,J}([d_1,d_2])
 \sum_{m\le N/[d_1,d_2]}\psi_{I,J}(m).
\tag{24}
\]

Terms with `\psi_{I,J}([d_1,d_2])=0` simply vanish. Since `|g(d)|\le1`, there are at most `B^2` inner sums, and every surviving interval length obeys

\[
Y:=\frac{N}{[d_1,d_2]}
\ge \frac{N}{B^2}
\gg y^{1-2b}.
\tag{25}
\]

If `q_{I,J}<Y`, the ordinary Polya--Vinogradov bound gives a fixed power saving because

\[
\left|\sum_{m\le Y}\psi_{I,J}(m)\right|
\ll \sqrt{q_{I,J}}\log q_{I,J}
\ll Y^{1/2}\log y.
\tag{26}
\]

If instead `q_{I,J}\ge Y`, then `(23)`, `(4)`, and `(25)` give

\[
q_{I,J}\le y^A,
\qquad
q_{I,J}^\delta
\ge y^{\delta(1-2b)}
>y^\theta
\ge P^+(q_{I,J}),
\tag{27}
\]

so `q_{I,J}\in\mathcal N(q_{I,J}^\delta)`. Also by `(16)`, `(19)`, and `(25)`,

\[
q_{I,J}^{\delta(1+\epsilon)}
\le y^{A\delta(1+\epsilon)}
<y^{1-2b}
\ll Y.
\tag{28}
\]

Thus `(17)` applies to the inner sum.

Combining the two cases and `(19)`, there exists a fixed `c=c(A)>0` such that uniformly for every off-diagonal pair in `W`,

\[
\boxed{
|S_{I,J}|\ll y^{1-c}.
}
\tag{29}
\]

Indeed, the smooth-modulus case contributes at most

\[
B^2N^{1-\eta}
\ll y^{1+2b-\eta},
\]

while the Polya--Vinogradov case contributes at most

\[
B^2N^{1/2}\log y
\ll y^{1/2+2b}\log y;
\]

both are `O(y^{1-c})` after the choices above.

This is the precise point where the 2026 near-linear smoothness threshold changes the source-cost frontier. Schlage-Puchta Proposition 9 inserts Burgess into `(24)` and therefore stops at the quadratic varying-modulus boundary. For the smooth subspace `W`, Cochrane--Granville--Zheng supplies a power saving at every fixed polynomial ambient modulus exponent.

## 3. Bombieri's frame inequality contradicts the endpoint rank

Let `A_y=|\mathcal R_y|`. The fixed progression prime number theorem gives

\[
A_y\asymp\frac y{\log y}.
\tag{30}
\]

Form the `H\times A_y` shell-character matrix

\[
V_{I,r}:=\chi_I(r),
\qquad I\in W,\ r\in\mathcal R_y.
\tag{31}
\]

Every row is constant on each of the `R` endpoint defect cells, so exactly as in `MC-374`,

\[
\operatorname{rank}V\le R.
\tag{32}
\]

No shell prime divides a lower-prime source modulus, hence every matrix entry has modulus one. For

\[
G:=A_y^{-1}VV^*,
\]

we therefore have

\[
\operatorname{tr}G=H,
\qquad
\lambda_{\max}(G)\ge\frac HR.
\tag{33}
\]

Now apply Bombieri's Hilbert-space lemma exactly as in the proof of Schlage-Puchta Theorem 3, but retain the pair-dependent off-diagonal bound `(29)` instead of replacing all pair moduli by a worst `Q^2`. On shell primes `r>y>B`, the Selberg weight satisfies `f(r)=1`, so the resulting quadratic-form estimate applies directly to arbitrary coefficient vectors supported on `\mathcal R_y`.

The diagonal term is bounded by Schlage-Puchta Lemma 8 / Proposition 9 as

\[
\ll \frac N{\log B}+B^2.
\tag{34}
\]

Every row has `H-1` off-diagonal inner products, each bounded by `(29)`. Hence

\[
\lambda_{\max}(VV^*)
\ll
\frac y{\log B}+B^2+Hy^{1-c}.
\tag{35}
\]

After division by `(30)`,

\[
\boxed{
\lambda_{\max}(G)
\ll_A
1+H y^{-c}\log y.
}
\tag{36}
\]

Combine `(33)` and `(36)`:

\[
\frac HR
\ll_A
1+H y^{-c}\log y.
\tag{37}
\]

It remains only to note that `R` is at most logarithmic in `y` under the assumed polynomial source package. The incidence vectors `V_1,\ldots,V_R` are linearly independent over `\mathbb F_2` because they represent independent endpoint functionals. Therefore

\[
R\le |U|\le\log_2P=O_A(\log y).
\tag{38}
\]

Also `(13)` and `R\to\infty` give

\[
H\ge2^{R-O_A(1)},
\qquad
\frac HR\to\infty.
\tag{39}
\]

Divide `(37)` by `H`. The first term on the right is `O_A(H^{-1})=o(R^{-1})`, while by `(38)`

\[
y^{-c}\log y=o(R^{-1}).
\tag{40}
\]

This contradicts the left side `1/R`. Therefore `(4)` is impossible for every fixed `A`, proving `(2)`--`(3)`.

## 4. Consequences for the current endpoint frontier

`MC-371` proved the defect-agnostic quartic lower floor

\[
\liminf\frac{\log P}{\log y}\ge4.
\]

The present result upgrades that finite floor to divergence:

\[
\boxed{
\frac{\log P}{\log y}\to\infty.
}
\tag{41}
\]

Therefore the quartic-saturation analyses in `MC-372`--`MC-376` remain valid as conditional structural theorems, but their common hypothesis `P=y^{4+o(1)}` cannot occur in an actual exact endpoint realization. In particular:

- the package/minimum-conductor concentration at exponent two from `MC-374` is now a conditional near-equality description of a regime that this finding excludes;
- the full-cube incidence delocalization of `MC-375` and the macroscopic inverse-root-rank bias at the quadratic boundary of `MC-376` remain exact deductions under quartic saturation, but they are no longer the live escape route;
- the natural lower-prime scale `Z\le y^{(1+o(1))/R}` is excluded a fortiori whenever the total package remains polynomial, independently of whether the package uses `2R`, `4R`, or any other `O(R)` number of source coordinates.

The surviving source-package branch must therefore pay **superpolynomial common radical cost** in the shell scale. This is qualitatively different from merely pushing most individual modes to conductor `y^{2-o(1)}`: the union of lower-prime source coordinates itself must escape every fixed power of `y`.

This does not by itself contradict the existence of lower-prime representatives. A product of sufficiently many primes below `y` can have superpolynomial size, and the argument gives no quantitative rate for the divergence in `(41)`. The next analytic question is whether the explicit moving-parameter form of the Cochrane--Granville--Zheng differencing method, together with source-incidence codimension, can make the divergence effective rather than only excluding each fixed polynomial exponent.

## Prior art and novelty boundary

The two analytic inputs are established literature mechanisms.

- Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143--149, Theorem 3 and its proof via Bombieri's lemma, Selberg's sieve, and Proposition 9. The proof explicitly reduces off-diagonal prime-frame control to weighted ordinary character sums after expanding `f=(1*g)^2`. `MC-323` and `MC-374` already use this prime-frame mechanism with Burgess as the inner character-sum input.
- Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026), especially Theorem 1 and Corollary 2, retained as `MC-S46`. Their result gives power-saving incomplete sums for nonprincipal characters when the ambient modulus is smooth essentially up to the interval scale. `MC-241` and `MC-242` already use that theorem in different shell-character problems.

A fresh targeted search on 18 September 2026 found the two ingredients and their separate applications but did not identify a published theorem phrased as the source-package conclusion `(2)`. No standalone novelty claim is made for the analytic inequality `(29)`: it is the direct Selberg-sieve composition of the cited smooth incomplete-sum theorem with Schlage-Puchta's established frame proof. The durable Mathia result is the exact endpoint/source-incidence consequence: finitely many rough source columns can be annihilated at only bounded codimension cost, leaving an exponentially large smooth mode subspace that the prime frame cannot support.

Cochrane--Granville--Zheng remains an arXiv v1 manuscript as of this audit, so theorem-level use here has the same manuscript evidence status already adopted in `MC-241`--`MC-242`.

## Boundaries and falsification tests

- **Exact endpoint structure is load-bearing.** The exponential subspace `W` comes from `R` independent endpoint generators whose source representatives combine by symmetric difference. A generic family of unrelated characters need not contain this kernel subspace.
- **The common source package is load-bearing.** The argument bounds every pair ambient lcm by one radical `P`. It does not say that the minimum primitive conductor of each endpoint mode is superpolynomial.
- **The conclusion is qualitative in the source exponent.** Each fixed `A` is excluded with constants depending on `A`; no uniform rate `A=A(y)->infinity` is obtained.
- **The 2026 smooth-modulus theorem is manuscript-level literature evidence.** If its Corollary 2 or parameter uniformity were materially revised, `(29)` would need re-audit.
- **The finite exceptional integer is removed, not ignored.** Source primes dividing `\mathcal M(\delta)` are added to `E_y`; this costs only bounded codimension and ensures every modulus used in the smooth subspace is coprime to the theorem's fixed exceptional integer.
- **Small pair moduli do not require the smooth theorem.** They are handled by Polya--Vinogradov in `(26)`; only pair moduli at least as large as their inner interval invoke Corollary 2.
- **No use of RH, GRH, a zero-free region, or the desired Möbius cancellation enters.** The result is a source-realizability obstruction local to the exact endpoint branch.
- **No estimate for `M(x)` follows.** Superpolynomial source cost narrows one candidate representation; it does not prove square-root cancellation.
