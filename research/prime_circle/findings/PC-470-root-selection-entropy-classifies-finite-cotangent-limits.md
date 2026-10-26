# PC-470 — Root-selection entropy classifies finite cotangent limits

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. Relative to uniform sampling of a retained primitive vertex, the exact leading entropy cost of a limiting rooted-support law is its expected number of additional vertices, in units of `log log y`. Every law of finite cost is attainable. Consequently a bounded multiple of this entropy scale cannot select an infinite admissible cotangent limit with positive probability. The entropy machinery and singular-series inputs are classical; this is a sharp selection boundary for the existing moving-center family, not a new large-deviation principle in general, a canonical selection rule, or an RH implication.

## 1. Sampling convention and sharp theorem

Let
\[
d_y=\prod_{p\le y}p,\quad N=d_y m,\quad m\ge1,\qquad
Y_{y,m}=\{c\bmod N:(c,d_y)=1\}.
\]
Write `U_(y,m)` for uniform probability on `Y_(y,m)`. Thus the center is already a retained vertex; the conditioning cost of retaining the root is **not** charged again. Put
\[
I_N=\{-N/2,\ldots,N/2-1\},\qquad
S_{y,m,c}=\{h\in I_N:(c+h,d_y)=1\}.
\tag{1}
\]
For `y>=2`, `N` is even and every support (1) contains zero. Work in the compact product space
\[
X_0=\{S\subset\mathbb Z:0\in S\},\qquad
\mathcal A_0=\{S\in X_0:|S\bmod p|<p\text{ for every prime }p\}.
\tag{2}
\]
The finite masks (1) need not belong to `A_0`: only primes up to `y` have been excluded. Every weak limit of their laws is supported on `A_0`, since a failure of admissibility has a finite modular witness.

A selector is any probability `Q_(y,m)` on `Y_(y,m)`. Its cost, in natural logarithms, is
\[
D(Q_{y,m}\Vert U_{y,m})
=\sum_{c\in Y_{y,m}}Q_{y,m}(c)
 \log\bigl(|Y_{y,m}|Q_{y,m}(c)\bigr).
\tag{3}
\]
Let `P_(y,m)` be its induced law of (1). For a probability `P` on `A_0`, define
\[
\mathcal J(P)=\int (|S|-1)\,dP(S)\in[0,\infty],
\tag{4}
\]
where an infinite support has infinite cost.

**Theorem.** Along any prescribed `y_j -> infinity` and any positive integer refinements `m_j`:

1. If `P_(y_j,m_j) => P`, then
   \[
   \boxed{\quad
   \liminf_j\frac{D(Q_{y_j,m_j}\Vert U_{y_j,m_j})}{\log\log y_j}
   \ge\mathcal J(P).
   \quad}
   \tag{5}
   \]
2. Every probability `P` on `A_0` admits selectors along that same sequence with `P_(y_j,m_j) => P` and
   \[
   \boxed{\quad
   \lim_j\frac{D(Q_{y_j,m_j}\Vert U_{y_j,m_j})}{\log\log y_j}
   =\mathcal J(P).
   \quad}
   \tag{6}
   \]
   The equality is in the extended nonnegative reals.

In particular, for finite `C`, the attainable limiting laws under the budget
`limsup D/log log y <= C` are exactly those with `E_P(|S|-1)<=C`.
This is a bound on expected cardinality, not an almost-sure bound `|S|<=C+1`.
Finite supports with infinite expected size also have infinite cost in (4).

## 2. Exact rooted cylinder probabilities

Fix `W_R=[-R,R]` and a subset `F subset W_R` containing zero, of size `k`.
For `N>2R`, CRT gives the exact inclusion probability
\[
p_y(F):=U_{y,m}(F\subset S_{y,m,c})
=\prod_{p\le y}\frac{p-\nu_p(F)}{p-1},
\qquad \nu_p(F)=|F\bmod p|.
\tag{7}
\]
The factor `m` cancels exactly, including when `m` shares primes with `d_y`.
If `F` is inadmissible, (7) is zero once the obstructing prime is included.
If `F` is admissible, write
\[
\eta_y=\prod_{p\le y}(1-1/p),\qquad
\mathfrak S(F)=\prod_p\frac{1-\nu_p(F)/p}{(1-1/p)^k}.
\tag{8}
\]
The latter product is positive and convergent: outside finitely many primes dividing differences, `nu_p(F)=k`, and its factors are `1+O_F(p^{-2})`.
Mertens's product theorem therefore yields
\[
p_y(F)\sim \mathfrak S(F)\eta_y^{k-1}
\sim \mathfrak S(F)e^{-(k-1)\gamma}(\log y)^{-(k-1)}.
\tag{9}
\]
These are exact finite-sieve counts followed by a classical product asymptotic; no prime-tuple conjecture is assumed.

The probability of the **exact** window is
\[
q_{y,R}(F):=U_{y,m}(S_{y,m,c}\cap W_R=F)
=\sum_{G\subset W_R\setminus F}(-1)^{|G|}p_y(F\cup G).
\tag{10}
\]
For each fixed `b in W_R\F`, either `F union {b}` is inadmissible, or (9) gives
\[
\frac{p_y(F\cup\{b\})}{p_y(F)}=O_{F,b}(\eta_y).
\]
A union bound, without any independence assumption, gives
\[
q_{y,R}(F)=p_y(F)(1+O_{F,R}(\eta_y)),\qquad
\frac{-\log q_{y,R}(F)}{\log\log y}\longrightarrow k-1.
\tag{11}
\]
For each fixed window this holds simultaneously over its finitely many admissible patterns, uniformly in all refinements. Inadmissible patterns eventually have probability zero. In particular every admissible exact window has positive probability eventually, even if it was absent at smaller cutoffs.

## 3. Entropy lower bound by finite partitions

Let `r_(j,R)` be the window law under the chosen selector. Grouping centers according to their exact window and applying the log-sum inequality gives
\[
D(Q_j\Vert U_j)\ge
\sum_F r_{j,R}(F)\log\frac{r_{j,R}(F)}{q_{y_j,R}(F)}.
\tag{12}
\]
Terms of zero mass are omitted. A selector cannot put mass on a window absent under `U_j`. For large `j`, all remaining patterns are admissible. There are at most `2^(2R)` rooted patterns, so
\[
\sum_F r_{j,R}(F)\log r_{j,R}(F)\ge-2R\log2.
\tag{13}
\]
Weak convergence of support laws gives convergence of every window probability, because cylinders are clopen. Divide (12) by `a_j=log log y_j` and use (11)–(13):
\[
\liminf_jD(Q_j\Vert U_j)/a_j
\ge\int(|S\cap W_R|-1)\,dP(S).
\tag{14}
\]
Only after taking this limit do we increase `R`. Monotone convergence proves (5), including infinite expected cardinality and positive mass on infinite supports. No estimate uniform in a growing window is silently assumed.

## 4. Recovery selectors attain the bound

Fix `P` on `A_0`, and let
\[
r_R(F)=P(S\cap W_R=F).
\]
For a fixed `R` and sufficiently large `y`, define a probability on centers by
\[
\frac{dQ^{(R)}_{y,m}}{dU_{y,m}}(c)
=\frac{r_R(F)}{q_{y,R}(F)},\qquad
F=S_{y,m,c}\cap W_R.
\tag{15}
\]
Assign density zero to patterns with `r_R(F)=0`. All patterns of positive `r_R` are admissible and have positive denominators eventually. This selector has **exactly** the target window law and remains uniform within each window class, including over the refinement lifts. Direct substitution gives equality in the partition cost:
\[
D(Q^{(R)}_{y,m}\Vert U_{y,m})
=\sum_F r_R(F)\log\frac{r_R(F)}{q_{y,R}(F)}.
\tag{16}
\]
Hence, for fixed `R`,
\[
D(Q^{(R)}_{y,m}\Vert U_{y,m})/\log\log y
\longrightarrow\mathcal J_R(P):=\int(|S\cap W_R|-1)\,dP(S).
\tag{17}
\]
Choose increasing thresholds `Y_R` so that for every `y>=Y_R` all required window classes exist, `d_y>2R`, and the error in (17) is at most `1/R`, uniformly in `m`. Along the prescribed sequence choose `R_j -> infinity` slowly enough that `y_j>=Y_(R_j)`. Equation (15) then matches every fixed window eventually, proving weak convergence to `P`. Since `J_R(P)` increases to `J(P)`, (16)–(17) prove (6).

For a deterministic finite admissible `F` containing zero, a simpler optimal selector conditions only on `F subset S`. Every additional fixed offset disappears in probability by the ratio preceding (11), so its support law tends to `delta_F`. Its cost is
\[
-\log p_y(F)
=(|F|-1)\log\log y+(|F|-1)\gamma-\log\mathfrak S(F)+o(1).
\tag{18}
\]
Thus a pair such as `{0,2}` has leading cost one, while the uniform rooted law has cost zero and tends to `{0}`. This verifies sharpness with a nonzero cotangent block, rather than merely an abstract recovery law.

## 5. Consequences for the actual cotangent operators

Use the unchanged embedded operators from
[[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]]:
\[
(K_{y,m,c})_{hk}=
\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(h-k)}N,&h,k\in S_{y,m,c},\ h\ne k,\\
0,&\text{otherwise}.
\end{cases}
\tag{19}
\]
Their norms are at most one. On an admissible limit support the operator is
\[
(L_S)_{hk}=\mathbf1_{h,k\in S}
\begin{cases}i/[\pi(h-k)],&h\ne k,\\0,&h=k.
\end{cases}
\tag{20}
\]
For a fixed column `k` and `R>|k|`, both kernels have squared column tails at most
`2/[pi^2(R-|k|)]`. On a fixed window their entries converge uniformly in the center and refinement once the masks agree. These are precisely PC-465's strong-convergence estimates. They also show that convergence in law of the masks implies convergence in distribution of (19) to (20), in the strong operator topology on the bounded operator ball. One can see this on finitely many columns first and then use their uniform norm bound. The augmented kernel differs in norm by `eta_y`, so it has the same conclusion.

It follows that:

- `D=o(log log y)` forces the support law to `delta_{ {0} }` and the operators strongly to zero in probability. For every fixed vector `v`, the bounded norms also give `E||K v||^2 -> 0`. The root spectral measure tends to `delta_0`.
- If `limsup D/log log y<=C<infinity`, every limiting support law is concentrated on finite admissible sets with `E(|S|-1)<=C`. Thus its retained limiting operators are finite dimensional almost surely. Their root spectral measures are atomic; their average is atomic too, since there are only countably many finite integer supports.
- A limiting law assigning positive mass to infinite supports forces `D/log log y -> infinity`. In particular, selecting a fixed infinite full-spectrum realization of PC-468 or PC-469, rooted at a retained vertex, requires that divergence.

The last assertion concerns the embedded limit operator/support. It does **not** exclude the full Hausdorff limit of the original finite spectra in PC-466: recentering never changes those spectra. Nor does atomicity mean a discrete closed spectral set, or forbid an ensemble average from having a large closed support. No operator-norm convergence follows from the first bullet.

## 6. Mathematical delta, controls and prior art

PC-458 already proves collapse of the uniform retained-vertex average, PC-465 classifies arbitrary moving-center limits, and PC-468/469 exhibit infinite realizations of very different spectral types. The additional result is an exact, attainable information cost for choosing among those limits. It closes the intermediate class of **all selectors with a bounded leading entropy cost**, rather than just uniform sampling or one prescribed center.

The leading cardinality price is universal rare-event geometry. Independent Bernoulli occupation with density `eta_y`, conditioned to retain zero, has the same leading cost `|F|-1` for every finite rooted pattern. The sieve changes the admissible support class and the singular-series constants in (18); those constants disappear after division by `log log y`. This comparison does not identify the two full laws, spectral sets, or finite constants, and supplies no prime-specific critical-line selector.

Closest sources and exact roles:

- K. S. Kedlaya, *Notes on analytic number theory*, Chapter 19, Definition 19.1, [source](https://kskedlaya.org/ant/chap-k-tuples.html). This is the standard singular-series normalization in (8). The CRT count itself already appears in PC-460, equation (6); rooting divides that count by the retained density. No conjecture about actual prime occurrences is used.
- J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, **Bull. Amer. Math. Soc. 50** (2013), 527–628, [author manuscript](https://arxiv.org/pdf/1303.1856), Theorem 3.3.2. Mertens's product asymptotic supplies the speed and constant in (9); this is the same classical input used in PC-458/460.
- M. Mariani, *A Gamma-convergence approach to large deviations*, **Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 18** (2018), 951–976, DOI [10.2422/2036-2145.201301_010](https://doi.org/10.2422/2036-2145.201301_010), [author manuscript](https://arxiv.org/pdf/1204.0640), Theorems 3.4–3.5. The equivalence between large-deviation bounds and normalized-relative-entropy lower/recovery bounds is classical. Equations (12)–(17) prove the required specialization directly using finite clopen partitions and conditional uniformity; no general entropy theorem is claimed as new.

Targeted local searches for relative entropy, large deviations, rooted/Palm selection and selection cost found no existing selector classification; the rooted occurrence counts in PC-153 and the finite-population laws PC-460/463 are related counting inputs, not this variational boundary. Structural literature searches covered reduced-residue/random-sieve patterns, rooted sampling and entropy recovery. The result is recorded as a classical-method specialization with explicit cotangent consequences, without a historical-priority claim.

## 7. Validation and evidence boundary

A standard-library Python audit made **1,408 exact checks** of rational inclusion–exclusion window probabilities and refinement multiplicities: prime cutoffs `5,7,11,13`, all rooted patterns in windows of radii one through four, and refinements `1,2,3`. It included absent patterns and refinements sharing sieve primes. **87** finite entropy checks tested exact-window conditioning, equality for the recovery selector and the log-sum lower bound for a selector nonuniform inside window classes. Maximum numerical discrepancies were below `8.4e-17` for the recovery chain formula and `4.5e-16` for conditioning cost. Scratch code remains under `/tmp`, outside Git.

These finite checks are normalization diagnostics. The limit theorem rests on the product convergence, fixed-window limits followed by monotone convergence, and slow diagonal recovery proved above. It is not Lean-verified or independently adversarially approved.

The scope is fixed integer-mesh coordinates, primorial sieves, retained-vertex reference sampling, and the unchanged conductor-scaled kernels. An entropy budget is a mathematical change-of-measure constraint, not a computation-time or model-token budget. Sampling from all ambient centers would charge the root as well. Changing the spatial scale, kernel, reference measure or asymptotic cost scale requires a new argument. Neither a geometry-forced selector nor new information on zeta zeros is supplied.

No compute or formalization executor is enrolled. The finite ingredients are classical and explicitly derived; the substantive boundary is the infinite-window variational limit, with no separate bounded formalization-fertility target asserted.
