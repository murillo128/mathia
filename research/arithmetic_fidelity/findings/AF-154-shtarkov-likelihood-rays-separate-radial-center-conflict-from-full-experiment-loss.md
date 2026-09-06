# AF-154 — Shtarkov likelihood rays separate radial center conflict from full experiment loss

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `POSITIVE-REFERENCE-CONSTRUCTION`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-149 introduced the finite Shtarkov/NML envelope as a prior-free common reference for whole-experiment recovery. AF-150--AF-153 then studied what happens when that center is propagated or recomputed after compression. The same construction has a sharper geometric interpretation that separates two distinct losses which those center calculations only partially exposed.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite set `X`. At each source point write the full family likelihood vector

\[
p(x):=(P_1(x),\ldots,P_m(x))\in\mathbb R_+^m,
\]

its pointwise envelope

\[
s(x):=\|p(x)\|_\infty=\max_iP_i(x),
\]

and the Shtarkov mass and center

\[
C:=\sum_xs(x),
\qquad
M(x):=\frac{s(x)}{C}.
\tag{1}
\]

On the union of the experiment supports define the **max-normalized likelihood ray**

\[
\boxed{
U(x):=\frac{p(x)}{s(x)}
=\left(\frac{P_1(x)}{s(x)},\ldots,\frac{P_m(x)}{s(x)}\right).
}
\tag{2}
\]

Then `U(x)` lies on the positive `ell_infinity` unit sphere:

\[
0\le U_i(x)\le1,
\qquad
\|U(x)\|_\infty=1.
\tag{3}
\]

The vector `U` is not an arbitrary normalization. It is a canonical representative of the projective likelihood class of `p(x)`: two source points have the same `U` exactly when their full likelihood vectors are positive scalar multiples of one another. Consequently, in this finite dominated setting, `U` is a minimal sufficient statistic for the experiment up to relabeling of its values. This is the classical likelihood-ratio criterion for minimal sufficiency written in the normalization selected by the Shtarkov envelope.

Now let

\[
K:X\rightsquigarrow Y
\]

be a stochastic compression, put

\[
Q_i=P_iK,
\qquad
q=MK,
\tag{4}
\]

and define the pushed source envelope

\[
\widetilde t(y):=\sum_xs(x)K(y\mid x)=Cq(y).
\tag{5}
\]

Under the reference joint law `M(x)K(y|x)`, the retained likelihood-ray vector is exactly

\[
\boxed{
V(y):=\mathbb E_M[U(X)\mid Y=y]
=\left(\frac{Q_1(y)}{\widetilde t(y)},\ldots,
\frac{Q_m(y)}{\widetilde t(y)}\right).
}
\tag{6}
\]

Thus stochastic compression first takes a **conditional barycenter of source likelihood rays**. That barycenter generally moves from the `ell_infinity` boundary into the positive unit cube.

Let

\[
t(y):=\max_iQ_i(y)
\tag{7}
\]

be the recomputed output envelope, and let

\[
W(y):=\frac{(Q_1(y),\ldots,Q_m(y))}{t(y)}
\tag{8}
\]

be the corresponding max-normalized output likelihood ray. Then

\[
\boxed{
\|V(y)\|_\infty
=\frac{t(y)}{\widetilde t(y)},
\qquad
W(y)=\frac{V(y)}{\|V(y)\|_\infty}.
}
\tag{9}
\]

Therefore the recanonicalization mechanism studied in AF-150--AF-153 has an exact geometry:

\[
\boxed{
\text{source likelihood rays}
\xrightarrow{\text{conditional averaging}}
V(y)\in[0,1]^m
\xrightarrow{\ell_\infty\text{-radial normalization}}
W(y).
}
\tag{10}
\]

In particular, AF-151's local max-sum conflict factor is precisely the radial normalization factor

\[
\boxed{
\kappa(y)
=\frac{\widetilde t(y)}{t(y)}
=\frac1{\|V(y)\|_\infty}.
}
\tag{11}
\]

This identifies exactly what `kappa` does and does not measure. It records the **radial shrinkage** of the conditional mean likelihood ray. It does not record the full conditional spread of `U`, nor changes among likelihood coordinates tangent to a face of the positive `ell_infinity` sphere.

The missing whole-experiment loss is supplied by AF-144/AF-149's Shtarkov-reference Pearson profile. Define

\[
\varepsilon_i^*(K)
:=
\chi^2(P_i\|M)-\chi^2(Q_i\|q).
\tag{12}
\]

Because

\[
\frac{P_i}{M}=C U_i,
\qquad
\frac{Q_i}{q}=C V_i,
\tag{13}
\]

the conditional-variance identity gives the exact formula

\[
\boxed{
\varepsilon_i^*(K)
=C^2\,\mathbb E_q\!\left[
\operatorname{Var}_M(U_i(X)\mid Y)
\right].
}
\tag{14}
\]

Summing over the family,

\[
\boxed{
\mathcal L_*(K;\mathcal E)
:=\sum_{i=1}^m\varepsilon_i^*(K)
=C^2\,\mathbb E_q
\|U(X)-V(Y)\|_2^2.
}
\tag{15}
\]

The zero boundary is exact:

\[
\boxed{
\mathcal L_*(K;\mathcal E)=0
\iff
K\text{ is sufficient for }\mathcal E.
}
\tag{16}
\]

Thus AF-149's warning about arbitrary external references has a useful specialization: although an arbitrary dominating reference gives only a one-way recovery certificate, the **Shtarkov reference itself restores the exact sufficiency zero set** because it is constructed homogeneously from the whole likelihood vector. Equivalently, its normalized coordinates `U` retain exactly the likelihood ray which classically defines minimal sufficiency.

Finally, radial conflict is quantitatively only a part of this full likelihood-ray loss. Since `U(X)` lies on `\{u\in[0,1]^m:\|u\|_\infty=1\}` while `V(y)` lies in the cube, for every output

\[
\mathbb E_M[
\|U-V(y)\|_2^2\mid Y=y]
\ge
\operatorname{dist}_2
\bigl(V(y),\{\|u\|_\infty=1\}\bigr)^2
=
(1-\|V(y)\|_\infty)^2.
\tag{17}
\]

Hence

\[
\boxed{
\mathcal L_*(K;\mathcal E)
\ge
C^2\,\mathbb E_q
\left(1-\frac1{\kappa(Y)}\right)^2.
}
\tag{18}
\]

There is no converse bound from `kappa` alone: one can have `kappa=1` everywhere, zero maximal-leakage drop, and exact Shtarkov-center commutation while `mathcal L_*>0` and the experiment is not sufficient. Such loss is **tangential likelihood-ray loss**: the same model remains the envelope winner throughout a compression fiber, so the radial statistic does not move, while non-maximal likelihood ratios still vary and are destroyed.

## Derivation

### The Shtarkov normalization is a canonical likelihood-ray representative

Suppose `s(x),s(x')>0`. Then

\[
U(x)=U(x')
\]

if and only if

\[
\frac{p(x)}{s(x)}=rac{p(x')}{s(x')},
\]

which is equivalent to

\[
p(x)=c\,p(x'),
\qquad
c=\frac{s(x)}{s(x')}>0.
\tag{19}
\]

For a finite dominated parameter family, proportionality of the complete likelihood vectors is the classical minimal-sufficiency equivalence relation. Thus `U` simply chooses the unique point on each positive likelihood ray whose largest coordinate is one.

For completeness, this can also be connected directly to the vector likelihood-ratio formulation of AF-013. Choose any full-support prior `lambda_i>0` on the labels and let

\[
G:=\sum_i\lambda_iP_i.
\tag{20}
\]

On the union of supports define

\[
L_i:=\frac{P_i}{G}.
\]

Then

\[
U_i
=\frac{L_i}{\max_jL_j}.
\tag{21}
\]

Conversely, because `sum_i lambda_i L_i=1`, `U` determines the full vector `L`:

\[
L_i
=\frac{U_i}{\sum_j\lambda_jU_j}.
\tag{22}
\]

So `U` and any complete reference-relative likelihood-ratio vector generate the same finite sufficient partition. The max normalization removes the auxiliary choice of `lambda` without discarding a likelihood direction.

### Compression averages likelihood rays

Under the reference law `M=s/C`,

\[
\begin{aligned}
\mathbb E_M[U_i(X)\mid Y=y]
&=
\frac{\sum_xM(x)K(y\mid x)U_i(x)}{q(y)}\\
&=
\frac{\sum_x\frac{s(x)}C K(y\mid x)\frac{P_i(x)}{s(x)}}
     {\widetilde t(y)/C}\\
&=
\frac{Q_i(y)}{\widetilde t(y)},
\end{aligned}
\tag{23}
\]

which proves `(6)`. Taking the maximum coordinate gives

\[
\|V(y)\|_\infty
=
\frac{\max_iQ_i(y)}{\widetilde t(y)}
=
\frac{t(y)}{\widetilde t(y)},
\]

and dividing `V` by that norm gives exactly `(8)`. This proves `(9)--(11)`.

The Shtarkov-mass contraction from AF-149 also becomes a one-line radial statement. If

\[
C_Y:=\sum_y t(y),
\]

then from `t=Cq\|V\|_\infty`,

\[
\boxed{
\frac{C_Y}{C}
=
\mathbb E_q\|V(Y)\|_\infty
=
\mathbb E_q\frac1{\kappa(Y)}.
}
\tag{24}
\]

Thus maximal-leakage loss sees only the mean radial retreat of the retained likelihood ray. AF-151's propagated-versus-recomputed center formula is likewise recovered because, for the recomputed center `r=t/C_Y`,

\[
\frac{r(y)}{q(y)}
=
\frac{\|V(y)\|_\infty}
     {\mathbb E_q\|V(Y)\|_\infty}.
\tag{25}
\]

### The Shtarkov Pearson profile is the full quadratic likelihood-ray defect

From `(13)`, Pearson divergence is simply the squared centered `L^2` norm of `C U_i` under `M`, while its output version is the squared norm of the conditional expectation `C V_i`. Orthogonal projection therefore gives

\[
\begin{aligned}
\varepsilon_i^*(K)
&=C^2\left(
\mathbb E_M U_i^2
-
\mathbb E_q V_i^2
\right)\\
&=C^2\,
\mathbb E_q\operatorname{Var}_M(U_i\mid Y),
\end{aligned}
\tag{26}
\]

proving `(14)`. Summing coordinates proves `(15)`.

If `mathcal L_*=0`, every `U_i` is constant on every posterior support generated by `K` under `M`. Since `P_i/M=C U_i`, the Shtarkov Bayes reverse

\[
R_M(x\mid y)
=\frac{M(x)K(y\mid x)}{q(y)}
\tag{27}
\]

then reconstructs every `P_i`; hence `K` is sufficient.

For the converse, assume `K` is sufficient for the declared finite experiment. Use the mixture `G` from `(20)`. By AF-013/classical finite sufficiency, the full vector `L=(P_i/G)_i` is constant on each posterior support of `K` under `G`. Equation `(21)` makes `U` a function of that same retained vector, so `U` is constant there as well. Because `G` and `M` have exactly the same support on the union of experiment supports, the relevant channel supports coincide. Therefore every conditional variance in `(14)` vanishes, proving `mathcal L_*=0` and `(16)`.

This also shows that exact sufficiency forces the Shtarkov reference to be compatible with the sufficient reduction even though it generally lies outside the convex hull of the experiment. The generic arbitrary-reference caveat in AF-149 remains correct; the envelope is special because `M/G=(max_iL_i)/C` is itself a function of the retained likelihood vector.

### Radial loss is a lower-dimensional projection of full loss

For fixed `y`, let

\[
v=V(y).
\]

Every conditional source value `U(X)` lies on the positive `ell_infinity` unit sphere. The Euclidean distance from `v in [0,1]^m` to that boundary is

\[
1-\|v\|_\infty:
\]

the nearest boundary point is obtained by raising any maximal coordinate of `v` to one. Therefore every source ray in the conditional support lies at Euclidean distance at least `1-||v||_infinity` from `v`, and averaging squared distances proves `(17)--(18)`.

The inequality can be very loose because radial displacement ignores motion parallel to a cube face. If one coordinate of `U` is identically one throughout a fiber while another coordinate varies, then the conditional mean still has `ell_infinity` norm one, so `kappa=1`, but the varying coordinate contributes strictly positive conditional variance to `(15)`.

## Exact arithmetic/analytic stress test: a local Euler factor

The tangential-loss mechanism already occurs in the prime-power data of one ordinary rational prime, without any generalized-prime construction.

Fix `p=2` and truncate the local Euler-factor weights to exponents `k=1,2,3`. Compare the two normalized real-half-plane profiles

\[
P_{\sigma}(k)
:=
\frac{2^{-\sigma k}}
     {\sum_{j=1}^3 2^{-\sigma j}}
\qquad
(\sigma=1,2).
\tag{28}
\]

The common factor `log 2` appearing in the corresponding local `-zeta'/zeta` prime-power weights would cancel under the same normalization. Explicitly,

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right).
\tag{29}
\]

Let the compression retain `k=1` but merge the higher prime powers `k=2,3` into one output. The source envelope is

\[
s=\left(\frac{16}{21},\frac27,\frac17\right),
\qquad
C=\frac{25}{21},
\]

so

\[
M=\left(\frac{16}{25},\frac6{25},\frac3{25}\right).
\tag{30}
\]

The two max-normalized likelihood rays are

\[
U_1=\left(\frac34,1,1\right),
\qquad
U_2=\left(1,\frac23,\frac13\right).
\tag{31}
\]

At the retained singleton `k=1`,

\[
V=\left(\frac34,1\right).
\]

On the merged tail, the Shtarkov conditional weights of `k=2,3` are `2/3,1/3`, hence

\[
V=\left(1,\frac59\right).
\tag{32}
\]

Both retained vectors still have `ell_infinity` norm one. Therefore

\[
\boxed{
\kappa\equiv1,
\qquad
C_Y=C,
\qquad
q=r.
}
\tag{33}
\]

The maximal-leakage/Shtarkov-mass audit and the center-drift audit both report **no loss at all**. Nevertheless `U_2` takes the distinct values `2/3` and `1/3` on the merged higher-prime-power fiber, so the experiment is not sufficient. The exact Shtarkov Pearson losses are

\[
\varepsilon_1^*=0,
\qquad
\boxed{
\varepsilon_2^*=\frac{50}{3969}>0.
}
\tag{34}
\]

The Shtarkov Bayes reverse splits the merged tail in the source-reference ratio `2:1`; for `P_2` it returns

\[
\left(\frac{16}{21},\frac{10}{63},\frac5{63}\right)
\]

instead of

\[
\left(\frac{16}{21},\frac{12}{63},\frac3{63}\right),
\]

with total-variation error

\[
\frac2{63}>0.
\tag{35}
\]

This is not an isolated numerical accident. For any fixed rational prime `p`, finite exponent range, and `sigma_a<sigma_b`, the likelihood ratio of the corresponding normalized local geometric laws has the form

\[
\frac{P_{\sigma_b}(k)}{P_{\sigma_a}(k)}
=
\frac{Z_{\sigma_a}}{Z_{\sigma_b}}
\,p^{-(\sigma_b-\sigma_a)k},
\tag{36}
\]

which is strictly decreasing in `k`. If a coarse-graining merges two or more exponents lying entirely on one side of the unique dominance crossing, the same member remains the envelope winner throughout that block, so `kappa=1` on the block, while the likelihood ratio varies strictly and exact sufficiency fails. Partitioning only along dominance regions can therefore preserve the full Shtarkov mass and center while still erasing prime-power exponent information relevant to the analytic parameter `sigma`.

The stress test gives the abstract distinction an arithmetic meaning: **preserving which local Euler-factor profile wins is weaker than preserving the ratios by which it wins.** A later RH-facing compression cannot use maximal-envelope identity or center stability alone as evidence that the prime-power analytic discriminator survived.

## Prior art and novelty assessment

The ingredients are established mathematics and the finding makes no theorem-level novelty claim.

- The proportional-likelihood characterization of minimal sufficiency is classical; AF-013 already records it in finite vector-likelihood-ratio form, with Lehmann--Casella and multiclass experiment references. In the present finite setting there is no Radon--Nikodym version ambiguity.
- Yuri M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175--186 (1987), is the classical source for the normalized maximum-likelihood envelope and minimax regret used in AF-149.
- Li Gao, Haojian Li, Iman Marvian, and Cambyse Rouze, **“Sufficient Statistic and Recoverability via Quantum Fisher Information,”** *Communications in Mathematical Physics* 405, article 180 (2024), DOI `10.1007/s00220-024-05053-z`, supplies the stronger Petz/chi-square recoverability context specialized to the finite commutative setting in AF-144.
- Ibrahim Issa, Aaron B. Wagner, and Sudeep Kamath, **“An Operational Approach to Information Leakage,”** *IEEE Transactions on Information Theory* 66(3), 1625--1657 (2020), DOI `10.1109/TIT.2019.2962804`, identifies the Shtarkov sum with the order-infinity/maximal-leakage quantity used in AF-150.

A targeted literature search for NML/Shtarkov centers under sufficient statistics and for maximal-leakage equality under sufficient reductions did not locate the exact combined presentation `(2)--(18)`. The projective-likelihood idea, minimal sufficiency, conditional expectation, Pearson projection identity, NML center, and maximal-leakage interpretation are all classical separately. The durable contribution here is therefore an **organizing equivalence**: the same max-normalized likelihood ray is simultaneously the prior-free minimal-sufficiency coordinate selected by the Shtarkov envelope, the object conditionally averaged by compression, and the object whose `ell_infinity` radial retreat generates AF-151's center-conflict scalar. No claim is made that this packaging is absent from the broader statistics or MDL literature.

## Boundary conditions and falsification tests

1. **Finite support is essential to the present statement.** The pointwise likelihood vector and Shtarkov center are unambiguous on a finite union of supports. Continuous models can have divergent Shtarkov integrals and version-dependent density representatives; those extensions need separate hypotheses.

2. **`U` is minimal sufficient for the declared finite family, not a universal coordinate for arbitrary downstream goals.** Adding or removing controls changes the likelihood ray. An arithmetic application must derive its matched-control family before treating `U` as canonical.

3. **Exact zero and approximate calibration remain different questions.** Equation `(16)` gives the correct zero set, while AF-149's private-label family shows that quantitative recovery can scale differently from Pearson loss. `mathcal L_*` is a sufficient quadratic certificate, not a universal metric equivalent to Le Cam deficiency.

4. **`kappa=1` is only a common-winner condition.** It means the conditional mean likelihood ray remains on an `ell_infinity` face; equivalently, at least one envelope-maximizing label survives across each local mixture. It does not make the complete likelihood ray constant. The Euler-factor example is the decisive control.

5. **Exact center commutation is weaker still.** AF-151 gives `q=r` when `kappa` is merely constant, even if that constant exceeds one. Therefore the hierarchy is strict in general:

\[
\text{full likelihood-ray sufficiency}
\Longrightarrow
\kappa=1
\Longrightarrow
q=r,
\tag{37}
\]

while neither converse holds.

6. **The arithmetic test is local, not an RH result.** It uses genuine rational-prime Euler-factor weights only to falsify an overstrong abstract inference. It does not show that this particular exponent coarse-graining occurs in a proposed global RH mechanism.

7. **Radial lower bound is one-way.** Equation `(18)` says large radial retreat forces some quadratic likelihood loss. Tangential loss can be arbitrarily substantial while the radial term vanishes, so no recovery theorem may replace the full profile by `kappa` without additional hypotheses controlling face-tangent variation.

## Consequence for Arithmetic Fidelity

The Shtarkov sequence now has a clean information geometry. The source family likelihood vector factors canonically as

\[
p(x)=s(x)U(x),
\tag{38}
\]

where `s` is envelope magnitude and `U` is the prior-free likelihood ray carrying the complete finite-experiment discriminator. Compression sends `U` to its conditional barycenter `V`; recomputing the Shtarkov object keeps the direction of `V` but radially normalizes it back to the `ell_infinity` boundary. AF-151's `kappa` measures only that radial correction.

This resolves an ambiguity in the current frontier. **Canonical-center stability and whole-experiment fidelity are not merely two differently calibrated scalar metrics; they observe different components of the retained likelihood geometry.** The former sees radial conflict among envelope winners. The latter requires the entire likelihood ray, including tangential variation among non-maximal coordinates.

For later prime-specific use, an audit should therefore ask two separate questions before any canonical reset: whether the prime-derived likelihood ray itself remains recoverable, and whether the chosen canonical center moves. Passing the second test cannot substitute for the first. The local Euler-factor control shows that this distinction already matters inside ordinary rational-prime prime-power data.