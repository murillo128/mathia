# NB-129 — target-bearing natural-grid phase visibility has a sharp reciprocal-height defect threshold

**Status:** `EXACT-DERIVED + TARGET-BEARING-NATURAL-GRID-VISIBILITY + SHARP-RECIPROCAL-HEIGHT-THRESHOLD + MATCHED-CONTROL + NB-117-NB-128-BRIDGE + FIXED-CAPTURE-BOUNDARY + PRIOR-ART-AUDITED`.

`NB-128` repairs the phase side of the finite-base alias obstruction: on the full natural prefix, a common vertical shift of size at most the section scale must create an order-one phase discrepancy somewhere. Its remaining caveat is load-bearing, however. For a zero-power primitive `P`, the translated sample difference is

\[
|P_T(n)-P(n)|=|P(n)|\,|n^{iT}-1|,
\]

so the phase witness can disappear if `P` is small at the integer where the phase modulus fires.

`NB-117` gives exactly the target-side information available to prevent that. A primitive with strong finite target capture is close, in weighted first-difference energy, to its endpoint-matched harmonic profile `C+D/n`. The splice between these two facts has a sharp scale: **natural-grid phase visibility at vertical scale `T` is forced once the target-angle defect is smaller than a constant times `1/T`, and the `1/T` threshold cannot be improved from the `NB-117` energy data alone.**

More precisely, let `R>=64` and let `P(1),...,P(R)` be any complex sequence with

\[
A:=P(1)-P(R)\ne0,
\qquad
L_R:=1-\frac1R.
\tag{1}
\]

Let

\[
H(n)
:=
P(R)+\frac{A}{L_R}
\left(\frac1n-\frac1R\right)
=C+\frac Dn,
\qquad
D=\frac{A}{L_R},
\tag{2}
\]

be the unique harmonic profile with the same endpoints, and write

\[
r(n):=P(n)-H(n),
\qquad
\mathcal E_R(r)
:=
\sum_{n<R}n(n+1)|r(n)-r(n+1)|^2.
\tag{3}
\]

For an integer `m>=16` with `2m<=R` and a real phase shift satisfying

\[
m\le |T|\le2m,
\tag{4}
\]

define the amplitude-weighted phase visibility on the matching natural block by

\[
\mathcal V_{m,T}(P)
:=
\sum_{n=m}^{2m}
|P(n)|^2|n^{iT}-1|^2.
\tag{5}
\]

Put

\[
\sigma_*:=
\sin\!\left(\frac12\log\frac32\right)>0.
\tag{6}
\]

Then the deterministic block inequality is

\[
\boxed{
\mathcal V_{m,T}(P)
\ge
\frac{\sigma_*^2}{2450}
\frac{|A|^2}{L_R^2m}
-
8\mathcal E_R(r).
}
\tag{7}
\]

The `NB-117` Pythagorean identity turns this into a target-angle statement. Define the single-vector capture fraction

\[
q_R(P)
:=
\frac{|A|^2}
{L_R\sum_{n<R}n(n+1)|P(n)-P(n+1)|^2}
\in(0,1].
\tag{8}
\]

Then

\[
\mathcal E_R(r)
=
\frac{|A|^2}{L_R}
\left(q_R(P)^{-1}-1\right),
\tag{9}
\]

and hence

\[
\boxed{
\frac{\mathcal V_{m,T}(P)}{|A|^2}
\ge
\frac{\sigma_*^2}{2450m}
-
16\left(q_R(P)^{-1}-1\right).
}
\tag{10}
\]

In particular,

\[
q_R(P)^{-1}-1
\le
\frac{\sigma_*^2}{78400m}
\tag{11}
\]

forces

\[
\boxed{
\mathcal V_{m,T}(P)
\ge
\frac{\sigma_*^2}{4900}
\frac{|A|^2}{m}.
}
\tag{12}
\]

Since `m` is comparable to `|T|`, this is an inverse-height visibility law. For every `32<=|T|<=R-2`, taking `m=ceil(|T|/2)` keeps the witnessing block inside the natural prefix and gives

\[
\mathcal V_{m,T}(P)
\gg
\frac{|A|^2}{|T|}
\tag{13}
\]

whenever the target-angle defect is at most a sufficiently small constant times `1/|T|`.

The scale is sharp in the exact ambient sequence model of `NB-117`. For every `m>=16` and `R>=4m` there is an endpoint-normalized sequence with

\[
\frac1{2m}
\le
q_R(P)^{-1}-1
\le
\frac3m
\tag{14}
\]

but

\[
\boxed{P(n)=0\qquad(m\le n\le2m),}
\tag{15}
\]

so `mathcal V_(m,T)(P)=0` for **every** phase shift. Thus an `O(1/T)` amount of excess target energy is already enough to erase an entire phase-sensitive block. The natural-grid phase modulus cannot be promoted to an order-one target-capture theorem by the `NB-117` Dirichlet energy alone.

For actual finite zero-power packets, `(7)`--`(13)` are source-faithful whenever `P=P_f` is their target-tail primitive. They show that near-perfect target capture at reciprocal-height accuracy prevents a common vertical translation from hiding behind amplitude zeros on the natural grid. But fixed positive capture `q_R(P)>=c<1` leaves a constant angle defect, far above the `1/T` threshold at large height. **This is the new boundary:** `NB-128` solves phase de-aliasing locally, but reaching the order-one capture regime relevant to `NB-115`--`NB-116` still requires extra zero-power structure beyond the weighted first-difference energy—such as recurrence, analyticity, or a source-specific nonconcentration law that rules out the sharp matched control below.

## 1. Every edge in the matching block has an order-one relative phase jump

Write `Delta=|T|`; complex conjugation reduces the phase estimates to `Delta>=0`. For every integer `k` with

\[
m\le k<2m,
\]

the relative phase of the adjacent natural samples is

\[
\left|\left(\frac{k+1}{k}\right)^{i\Delta}-1\right|
=
2\sin\!\left(
\frac{\Delta}{2}\log\left(1+\frac1k\right)
\right),
\tag{16}
\]

because the phase angle lies strictly below `pi`. Indeed, using `Delta>=m`, `k<=2m`, and Bernoulli's inequality,

\[
\Delta\log\left(1+\frac1k\right)
\ge
m\log\left(1+\frac1{2m}\right)
\ge
\log\frac32.
\tag{17}
\]

The last step follows from

\[
\left(1+\frac1{2m}\right)^m
\ge1+\frac12=\frac32.
\]

On the other hand, `Delta<=2m`, `k>=m`, and `log(1+u)<=u` give

\[
\Delta\log\left(1+\frac1k\right)
\le2<\pi.
\tag{18}
\]

Therefore

\[
\left|\left(\frac{k+1}{k}\right)^{i\Delta}-1\right|
\ge2\sigma_*.
\tag{19}
\]

Let

\[
v_n:=n^{i\Delta}.
\]

Since

\[
|v_{k+1}-v_k|
\le|v_{k+1}-1|+|v_k-1|,
\]

`(19)` implies that every adjacent edge `(k,k+1)` has at least one endpoint satisfying

\[
|v_n-1|\ge\sigma_*.
\tag{20}
\]

Call such an integer **phase-visible**. There cannot be two consecutive phase-invisible integers anywhere in `[m,2m]`. This is stronger than the single-coordinate statement of `NB-128`: on a block whose index scale matches the height difference, order-one phase visibility has positive density.

## 2. An endpoint-matched harmonic profile cannot vanish on all visible cells

Split the block into two separated subblocks

\[
I_-:=
\left[m,\left\lfloor\frac{5m}{4}\right\rfloor\right],
\qquad
I_+:=
\left[\left\lceil\frac{7m}{4}\right\rceil,2m\right].
\tag{21}
\]

For `m>=16`, each contains at least `m/16` phase-visible integers because no two consecutive vertices are invisible.

The two harmonic clusters are uniformly separated. If `n in I_-` and `j in I_+`, then

\[
\left|\frac Dn-\frac Dj\right|
=
|D|\left(\frac1n-\frac1j\right)
\ge
\frac{8|D|}{35m}.
\tag{22}
\]

For arbitrary `C in C`, the point `-C` cannot lie within distance `4|D|/(35m)` of a member of **both** clusters: two such members would contradict `(22)` by the triangle inequality. Consequently, on at least one of `I_-` or `I_+`, every point satisfies

\[
\left|C+\frac Dn\right|
\ge
\frac{4|D|}{35m}.
\tag{23}
\]

Restricting to the at least `m/16` phase-visible integers in that subblock gives

\[
\begin{aligned}
\mathcal V_{m,T}(H)
&:=
\sum_{n=m}^{2m}
|H(n)|^2|n^{iT}-1|^2\\
&\ge
\frac m{16}\,
\left(\frac{4|D|}{35m}\right)^2
\sigma_*^2\\
&=
\boxed{
\frac{\sigma_*^2}{1225}\frac{|D|^2}{m}.
}
\end{aligned}
\tag{24}
\]

The constant term `C` therefore cannot provide the amplitude escape. Even if it cancels the `D/n` profile on one macroscopic part of the block, it necessarily leaves a comparable separated part visible.

The `1/m` size is already the correct dimensional scale: on `n asymp m`, a harmonic target profile has amplitude `asymp |D|/m` on `asymp m` samples.

## 3. The NB-117 Dirichlet defect controls the residual on the whole block

Because `r(R)=0`, Cauchy--Schwarz with the exact `NB-117` weights gives for every `n<R`

\[
\begin{aligned}
|r(n)|^2
&=
\left|
\sum_{k=n}^{R-1}(r(k)-r(k+1))
\right|^2\\
&\le
\mathcal E_R(r)
\sum_{k=n}^{R-1}\frac1{k(k+1)}\\
&=
\mathcal E_R(r)
\left(\frac1n-\frac1R\right)\\
&\le
\frac{\mathcal E_R(r)}n.
\end{aligned}
\tag{25}
\]

Hence

\[
\sum_{n=m}^{2m}|r(n)|^2
\le
\mathcal E_R(r)
\sum_{n=m}^{2m}\frac1n
<2\mathcal E_R(r).
\tag{26}
\]

For complex numbers `a,b`,

\[
|a+b|^2\ge\frac12|a|^2-|b|^2.
\tag{27}
\]

Multiplying `(27)` by `|n^(iT)-1|^2<=4`, summing, and using `(24)`--`(26)` yields

\[
\begin{aligned}
\mathcal V_{m,T}(P)
&\ge
\frac12\mathcal V_{m,T}(H)
-4\sum_{n=m}^{2m}|r(n)|^2\\
&\ge
\frac{\sigma_*^2}{2450}\frac{|D|^2}{m}
-8\mathcal E_R(r),
\end{aligned}
\]

which is `(7)` because `D=A/L_R`.

`NB-117` gives the exact orthogonal energy decomposition

\[
\sum_{n<R}n(n+1)|\Delta P(n)|^2
=
\frac{|A|^2}{L_R}+\mathcal E_R(r).
\tag{28}
\]

Substituting `(28)` into `(8)` proves `(9)`. Since `1/2<=L_R<1`, `(7)` then implies `(10)`, and `(11)` gives `(12)`.

This is the amplitude bridge missing from `NB-128`, but only at the accuracy scale displayed explicitly in `(11)`.

## 4. Reciprocal-height excess energy is enough to hide an entire phase block

The threshold cannot be improved in order using only the endpoint and weighted Dirichlet information of `NB-117`. Fix `m>=16`, `R>=4m`, and `D ne0`. Let the endpoint-matched harmonic profile be

\[
H(n):=D\left(\frac1n-\frac1m\right).
\tag{29}
\]

Define an endpoint-zero residual by

\[
r(n)=0,
\qquad 1\le n\le m,
\tag{30}
\]

\[
r(n)=D\left(\frac1m-\frac1n\right),
\qquad m\le n\le2m,
\tag{31}
\]

and, for `2m<=n<=R`, let `r` be the weighted-energy minimizing harmonic bridge from `r(2m)=D/(2m)` to `r(R)=0`:

\[
r(n)
=
\frac{D}{2m}
\frac{1/n-1/R}{1/(2m)-1/R}.
\tag{32}
\]

These formulas agree at both junctions and give `r(1)=r(R)=0`. Thus `H` is indeed the endpoint-matched harmonic profile of

\[
P:=H+r.
\]

But `(29)` and `(31)` cancel exactly on the whole middle block:

\[
P(n)=0
\qquad(m\le n\le2m),
\tag{33}
\]

so `(15)` follows.

The energy paid for that erasure is only reciprocal in the block scale. On the middle block,

\[
\sum_{n=m}^{2m-1}n(n+1)|\Delta r(n)|^2
=
|D|^2\sum_{n=m}^{2m-1}\frac1{n(n+1)}
=
\frac{|D|^2}{2m}.
\tag{34}
\]

The bridge `(32)` has the exact minimal energy

\[
\frac{|D|^2/(4m^2)}{1/(2m)-1/R}
\le
\frac{|D|^2}{m},
\tag{35}
\]

where `R>=4m` was used in the last step. Therefore

\[
\frac{|D|^2}{2m}
\le
\mathcal E_R(r)
\le
\frac{3|D|^2}{2m}.
\tag{36}
\]

Here `A=D L_R`, so `(9)` gives

\[
\frac1{2m}
\le
q_R(P)^{-1}-1
=
\frac{\mathcal E_R(r)}{|D|^2L_R}
\le
\frac3m,
\tag{37}
\]

proving `(14)`.

Thus the phase-amplitude bridge undergoes a genuine transition at reciprocal height. An `o(1/m)` target-angle defect is safely below the ambient hiding cost; a defect of order `1/m` can already buy complete invisibility on the whole matching block. Constants are not optimized, but the scale is exact.

## 5. Consequences for finite zero-power packets

For a finite packet vector `f` in the `NB-117` model, put `P=P_f`. The quantity `(8)` is exactly the fraction of the finite target direction captured by that vector after integer-cell compression. If the packet target angle `chi_(F,R)` is attained by `f`, then

\[
q_R(P_f)=\chi_{F,R}.
\tag{38}
\]

For a formal common vertical translation by `T`, `NB-128` gives

\[
P_{f,T}(n)=n^{iT}P_f(n),
\tag{39}
\]

so `(5)` is exactly the squared natural-grid sample discrepancy on the block:

\[
\mathcal V_{m,T}(P_f)
=
\sum_{n=m}^{2m}
|P_{f,T}(n)-P_f(n)|^2.
\tag{40}
\]

Equations `(10)`--`(13)` therefore turn the labelled phase separation of `NB-128` into **actual primitive-sample separation** whenever the packet captures the target to reciprocal-height angular accuracy.

The qualification is decisive. The source-facing regime left by `NB-115`--`NB-116` asks whether high actual zero packets can have **order-one** finite target access. A fixed lower bound `chi_(F,R)>=c>0` permits

\[
\chi_{F,R}^{-1}-1=O_c(1),
\]

which is much larger than `1/G` at height `G`. The matched control in Section 4 shows that the `NB-117` energy information alone cannot bridge that gap: an ambient primitive may spend only `Theta(1/G)` excess energy and erase every sample in the phase-sensitive `n asymp G` block.

Hence the next source theorem cannot merely repackage the natural-grid phase modulus. It must exploit a property absent from the matched control—most naturally the finite zero-power recurrence/confluence structure of `NB-123`--`NB-125`, or another analytic nonconcentration principle—to show that an actual packet cannot localize its entire `Theta(1/G)` excess energy so as to cancel the harmonic target profile on the relevant block.

This also separates two inverse-height quantities that should not be conflated. `NB-116` proves an `O(1/G)` **continuum target-mass/compression-retention** budget for high actual zeros. The present result proves a `Theta(1/G)` **discrete target-angle excess-energy threshold** for making phase information amplitude-visible. Their matching scale is structurally suggestive, but no equality or implication between those quantities is asserted here.

## 6. Adversarial and prior-art audit

The argument is finite and deterministic. The phase step uses only adjacent ratios on the matching block; it does not assume equidistribution, independence of `log n`, or a zero-spacing theorem. The harmonic lower bound explicitly permits an arbitrary complex constant `C`; two separated reciprocal clusters prevent a single `C` from cancelling both. The residual estimate uses the exact telescoping dual of the `n(n+1)` Dirichlet weights, so there is no hidden unweighted-to-weighted conditioning loss. The matched control satisfies the same endpoint normalization and weighted energy geometry and therefore genuinely tests what `NB-117` alone can force.

The control is **not** claimed to be a zero-power packet. That is precisely its role: it proves that the endpoint plus weighted-Dirichlet data do not rule out block invisibility at defect `Theta(1/m)`. Actual zero-power recurrence may still exclude the control, and proving such exclusion is now the source-specific frontier. Likewise, `(39)` concerns the formal common-translation family used in `NB-126`--`NB-128`; translating a packet of exponents does not assert that the translated exponents are again zeta zeros.

A targeted literature audit around the Nyman--Beurling/Báez-Duarte quantitative approximation problem, Burnol's zero-sensitive lower bounds, and later optimal-rate work finds the expected global approximation-rate and zero-obstruction results already anchored in `SOURCES.md`. No external theorem is used in `(7)`--`(37)`, and no priority claim is made for the elementary path/Dirichlet estimates individually. The line-local delta is their exact splice with the `NB-117` harmonic target geometry and `NB-128` natural-grid phase modulus, together with the matched control proving the reciprocal-height threshold sharp in the admitted ambient sequence model. No new literature dependency is therefore added to `SOURCES.md`.

The durable conclusion is narrower than an RH advance but stronger than a heuristic nonconcentration request: **phase stability becomes target-bearing only below a sharp reciprocal-height target-angle defect threshold if one uses the current Dirichlet-energy information alone.** Any route from the natural-grid phase modulus to fixed positive high-zero target capture must now use genuinely additional zero-power structure.