# MC-374 — Prime-frame rank forces central quadratic conductor saturation

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `DECISIVE-NEGATIVE` · `CONDUCTOR-SATURATION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint partition of `MC-296` and the source-character dictionary used in `MC-301`, `MC-323`, and `MC-372`. Let

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R
\]

be the prime shell split into the `R` nonempty defect cells, and let `\lambda_1,\ldots,\lambda_R` be the independent endpoint generators. For every nonzero endpoint mode

\[
\lambda_I=\sum_{i\in I}\lambda_i,
\qquad \varnothing\ne I\subseteq[R],
\]

write `\mathcal Q(\lambda_I)` for its minimum primitive lower-prime source conductor.

There is a stronger consequence of the varying-modulus prime Halász--Montgomery theorem than the scalar bias-energy bound used in `MC-323` and `MC-372`: **the theorem is a frame inequality for arbitrary prime-supported coefficients**. Combined with the fact that every endpoint character is constant on each of the `R` defect cells, this bounds the number of endpoint modes that can simultaneously have subquadratic primitive conductor, independently of their individual shell biases.

More precisely, fix `\delta\in(0,2)`. Let `\mathcal F` be any set of distinct nonzero endpoint modes satisfying

\[
\mathcal Q(\lambda)\le y^{2-\delta}
\qquad(\lambda\in\mathcal F),
\]

and put `m=|\mathcal F|`. Then there are constants `c_\delta,C_\delta>0` such that

\[
\boxed{
\frac mR
\le
C_\delta\left(1+m y^{-c_\delta}\log y\right).
}
\tag{1}
\]

Consequently, whenever

\[
R y^{-c_\delta}\log y=o(1),
\tag{2}
\]

one has the uniform cardinality bound

\[
\boxed{m=O_\delta(R).}
\tag{3}
\]

Thus an exact endpoint of rank `R` can have only linearly many fixed-subquadratic primitive source modes, even though it has `2^R-1` nonzero Fourier modes. This conclusion does **not** require the selected modes to have fixed nonzero prime-shell bias.

The moving-order Burgess audit of `MC-373` pushes the same frame-rank argument to a shrinking distance from the quadratic boundary. Put

\[
L=\log\log y,
\qquad
J=\log\log\log y,
\qquad
\Delta(y)=K\frac JL,
\tag{4}
\]

with the same sufficiently large fixed absolute `K` as in `MC-373`, and define

\[
\eta(y)
:=
\exp\!\left(-c\frac{(\log y)J}{L^2}\right)\log y
\tag{5}
\]

for the absolute `c>0` delivered there. If

\[
R\eta(y)=o(1),
\tag{6}
\]

then every family of endpoint modes with

\[
\mathcal Q(\lambda)\le y^{2-\Delta(y)}
\]

satisfies

\[
\boxed{
 m=O\!\left(\frac R{\Delta(y)}\right)
 =O\!\left(R\frac LJ\right).
}
\tag{7}
\]

Now assume `R` is even and consider the middle Hamming layer

\[
\mathcal C_R=\{I\subseteq[R]:|I|=R/2\},
\qquad
M_R=|\mathcal C_R|=\binom R{R/2}.
\tag{8}
\]

Equation `(7)` gives

\[
\boxed{
\#\left\{I\in\mathcal C_R:
\mathcal Q(\lambda_I)\le y^{2-\Delta(y)}
\right\}
=O\!\left(R\frac LJ\right).
}
\tag{9}
\]

Hence, as `R\to\infty`, all but an exponentially small fraction of the middle layer have primitive conductor **above** the effective near-quadratic threshold `y^{2-\Delta(y)}`.

This reverses the possible escape left open in `MC-372`. There, a high fixed package representative `m_I` could in principle admit a much cheaper primitive representative, and proving that almost all middle modes were fixed-subquadratic would have forced endpoint `L^2` defect balance. Equation `(9)` shows that this route is unavailable: the prime-frame inequality forces almost the entire middle layer to remain near the quadratic boundary instead.

Under the quartic source-saturation hypothesis of `MC-371`--`MC-372`, this statement becomes a genuine minimum-conductor saturation theorem. Assume

\[
\frac{\log P}{\log y}=4+o(1),
\qquad
\mathcal B_R=o(1).
\tag{10}
\]

For the canonical middle-layer package representatives

\[
m_I=\prod_{p\in V_I}p,
\]

`MC-372` gives

\[
\frac1{M_R}\sum_{I\in\mathcal C_R}\log m_I
=(2+o(1))\log y.
\tag{11}
\]

Since always

\[
\mathcal Q(\lambda_I)\le m_I,
\tag{12}
\]

combining `(9)`--`(12)` yields, for every fixed `\varepsilon>0`,

\[
\boxed{
\frac1{M_R}
\#\left\{I\in\mathcal C_R:
\left|\frac{\log m_I}{\log y}-2\right|>\varepsilon
\right\}
\longrightarrow0,
}
\tag{13}
\]

and also

\[
\boxed{
\frac1{M_R}
\#\left\{I\in\mathcal C_R:
\left|\frac{\log \mathcal Q(\lambda_I)}{\log y}-2\right|>\varepsilon
\right\}
\longrightarrow0.
}
\tag{14}
\]

Thus, in the quartic-saturated endpoint regime, the middle layer is not merely expensive in the chosen package: **its minimum primitive conductors themselves concentrate at exponent two.** The package/minimum-conductor distinction from `MC-372` survives only on a zero-density exceptional set at fixed exponent scale.

This is a structural narrowing, not a Möbius bound. It says that the current endpoint program cannot obtain defect balance by hoping that most central modes secretly collapse to fixed-subquadratic primitive conductors. Any further use of the middle layer must work at the quadratic boundary itself, use a different invariant, or strengthen the prime-character input beyond the present Burgess/Halász--Montgomery horizon. No estimate for `M(x)` follows.

## 1. The endpoint character matrix has rank at most `R`

For each `\lambda\in\mathcal F`, choose a minimizing lower-prime representative. As in `MC-301` and `MC-323`, it defines a distinct primitive real character `\chi_\lambda` of odd squarefree conductor

\[
q_\lambda=\mathcal Q(\lambda),
\]

and on every shell prime `r\in\mathcal R_y`,

\[
\chi_\lambda(r)=(-1)^{\lambda(s(r))}.
\tag{15}
\]

Let `A_y=|\mathcal R_y|` and form the `m\times A_y` matrix

\[
V_{\lambda,r}=\chi_\lambda(r).
\tag{16}
\]

The exact endpoint partition is pointwise stronger than the averaged identity used in `MC-372`: each endpoint mode is constant on every cell `D_j`. Therefore every row of `V` belongs to the `R`-dimensional subspace of functions on `\mathcal R_y` that are constant on the cells `D_1,\ldots,D_R`. Hence

\[
\boxed{\operatorname{rank}V\le R.}
\tag{17}
\]

Normalize the row Gram matrix by

\[
G:=A_y^{-1}VV^*.
\tag{18}
\]

No shell prime divides a lower-prime source conductor, so every entry of every row has modulus one. Thus

\[
\operatorname{tr}G=m.
\tag{19}
\]

Since `G` is positive semidefinite and has rank at most `R`,

\[
\boxed{
\lambda_{\max}(G)\ge\frac mR.
}
\tag{20}
\]

This lower bound uses no information about the scalar averages `x_\lambda`. Central modes may have tiny or zero mean and still contribute one unit to the trace of the frame Gram matrix.

## 2. Schlage-Puchta gives the matching frame upper bound

Theorem 3 of Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arith. 106 (2003), 143--149, is stated for arbitrary prime-supported coefficients. The varying-modulus clause used in `MC-323` replaces the common modulus by `Q^2`; when the individual moduli are cubefree, their pairwise lcm is cubefree and arbitrary fixed Burgess order is available.

Therefore, for every coefficient vector `a=(a_r)_{r\in\mathcal R_y}`, the same parameter choices used in `MC-323` give

\[
\sum_{\lambda\in\mathcal F}
\left|\sum_{r\in\mathcal R_y}a_r\chi_\lambda(r)\right|^2
\le
C_\delta A_y
\left(1+m y^{-c_\delta}\log y\right)
\sum_{r\in\mathcal R_y}|a_r|^2.
\tag{21}
\]

Equation `(21)` is exactly an operator-norm bound for `V`, and hence

\[
\boxed{
\lambda_{\max}(G)
\le
C_\delta\left(1+m y^{-c_\delta}\log y\right).
}
\tag{22}
\]

Combining `(20)` and `(22)` proves `(1)`. If `(2)` holds, then for sufficiently large `y`,

\[
C_\delta R y^{-c_\delta}\log y\le\frac12.
\]

Multiplying `(1)` by `R` and absorbing the term proportional to `m` gives

\[
m\le2C_\delta R,
\]

which is `(3)`.

The distinction from `MC-323` is important. `MC-323` inserted the single coefficient vector `a_r=1` and therefore controlled the **sum of squared scalar shell biases**. Here the primary theorem is used before choosing `a`: its coefficient-uniform form controls the largest eigenvalue of the entire restricted character Gram matrix. The rank defect `(17)` then supplies the lower eigenvalue pressure even when every scalar shell bias in the selected family is small.

## 3. The moving-order audit survives at operator level

The derivation in `MC-373` tracks every dependence on the Burgess order through the explicit cubefree Burgess theorem, imprimitive reduction, and Schlage-Puchta's Selberg-sieve convolution. None of those bounds depends on choosing `a_r=1`; Schlage-Puchta's theorem remains a quadratic-form inequality for arbitrary prime-supported coefficients.

Thus the same choices

\[
r=\left\lfloor\frac L{32}\right\rfloor,
\qquad
\Delta(y)=KJ/L
\]

give the coefficient-uniform bound

\[
\lambda_{\max}(G)
\ll
\frac1{\Delta(y)}+m\eta(y),
\tag{23}
\]

with `\eta(y)` from `(5)`. Combining `(20)` and `(23)` gives

\[
\frac mR
\ll
\frac1\Delta+m\eta.
\tag{24}
\]

Under `(6)` the second term is absorbed, proving `(7)`.

The 2025 explicit Burgess manuscript used by `MC-373` was rechecked during this audit. As of 18 September 2026, arXiv `2511.17778` still exposes version 1 dated 21 November 2025, and Enrique Treviño's current publication list still describes the work as submitted. It is therefore used with the same manuscript-level evidence status as in `MC-373`, not as a peer-reviewed theorem source.

## 4. Central-layer primitive conductors concentrate at exponent two

Apply `(7)` to the low-conductor subfamily of the middle layer. This gives `(9)`. Because

\[
M_R
=2^R\sqrt{\frac{2}{\pi R}}(1+o(1)),
\tag{25}
\]

one has

\[
\frac{R L/J}{M_R}\longrightarrow0
\tag{26}
\]

whenever `R\to\infty`. Hence, outside a zero-density exceptional set,

\[
\frac{\log\mathcal Q(\lambda_I)}{\log y}
>2-\Delta(y).
\tag{27}
\]

Under `(10)`, equation `(11)` supplies the mean package exponent. Put

\[
a_I:=\frac{\log m_I}{\log y}.
\]

Outside the exceptional set in `(9)`, `(12)` and `(27)` give

\[
a_I>2-\Delta(y).
\tag{28}
\]

Let `u_R(\varepsilon)` be the fraction of middle-layer indices with

\[
a_I>2+\varepsilon.
\]

Using `a_I\ge0` on the exceptional set and `(28)` elsewhere,

\[
2+o(1)
\ge
(1-o(1)-u_R)(2-\Delta)
+u_R(2+\varepsilon).
\tag{29}
\]

Since `\Delta(y)\to0`, equation `(29)` implies

\[
u_R(\varepsilon)\to0.
\tag{30}
\]

The lower-tail fraction for `a_I<2-\varepsilon` is already contained in the exceptional set once `\Delta<\varepsilon`. This proves `(13)`.

For the minimum conductor, the lower tail

\[
\mathcal Q(\lambda_I)<y^{2-\varepsilon}
\]

is again contained in the exceptional set for large `y`, while the upper tail

\[
\mathcal Q(\lambda_I)>y^{2+\varepsilon}
\]

is contained in the package upper tail because of `(12)`. Equation `(14)` follows.

Thus the central package has a stronger near-equality structure than `MC-372` could certify from package cost alone: both the chosen representative and the true minimum primitive representative concentrate at the same quadratic exponent.

## 5. Prior art and novelty boundary

The analytic inequality is classical prior art. The primary source is Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143--149; arXiv `1105.1623`. The primary PDF was rechecked for this finding: its proof of Theorem 3 explicitly treats characters belonging to different moduli and notes that the pairwise lcm stays cubefree when the individual moduli are cubefree. The theorem is a quadratic-form inequality for arbitrary prime-supported coefficients, so the frame interpretation in `(21)`--`(22)` does not strengthen Schlage-Puchta's analytic result.

The moving-order input is Elchin Hasanalizade, Hua Lin, Greg Martin, Andradis Luna Martínez and Enrique Treviño, *Explicit Burgess inequalities for cubefree moduli*, arXiv `2511.17778v1` (21 November 2025), already audited in `MC-373`. No new Burgess estimate is claimed.

The passage from a quadratic-form inequality to a largest-eigenvalue bound, and the trace/rank inequality `lambda_max >= trace/rank`, are elementary operator/linear algebra. Large-sieve inequalities are classically viewed as spectral bounds for their associated Gram matrices. A targeted literature search found no reason to treat this frame reformulation as new mathematics.

**No standalone novelty claim is made.** The durable Mathia delta is the composition at the current endpoint frontier: exact defect-cell geometry forces rank at most `R`; the coefficient-uniform varying-modulus prime theorem bounds the same frame from above; and the moving-order audit then shows that only `O(RL/J)` of the exponentially many central endpoint modes can lie below `y^{2-KJ/L}`. Under quartic package saturation, this closes the density-level package/minimum-conductor escape left explicit in `MC-372`.

## 6. Boundaries and falsification tests

- **Exact partition is load-bearing.** The rank bound `(17)` uses that every endpoint character is constant on the same `R` defect cells. Overlapping or non-partition defect structures can have a larger restricted row space and require a different rank parameter.
- **Primitive cubefree representatives are load-bearing.** The varying-modulus arbitrary-order theorem is applied to the minimizing odd squarefree lower-prime representatives. A different source dictionary must recheck this condition.
- **The family must contain distinct characters.** Distinct endpoint functionals admit distinct selected primitive representatives by the source-character injectivity already audited in `MC-301`. Repeated copies cannot create rank pressure.
- **The absorption condition is explicit.** The fixed-deficit statement needs `(2)`. The moving-order statement needs `(6)`, equivalently enough separation that the theorem's family-size error is small on the `R`-dimensional endpoint row space. The critical endpoint ranks of order `\log\log y` satisfy this easily, but arbitrary `R=y^{o(1)}` is not asserted to satisfy the moving-order condition.
- **The conclusion is scarcity, not cancellation.** Equations `(3)` and `(7)` show that low-conductor endpoint modes are rare. They do not show that high-conductor modes have small shell bias.
- **Defect balance is not recovered.** In fact the conclusion kills the specific sufficient route in `MC-372`: almost all central modes are forced onto the high-conductor side of its balance-versus-conductor dichotomy. No estimate for `\Delta_2` follows from that dichotomy.
- **Quadratic saturation is conditional on quartic package saturation.** Equations `(13)`--`(14)` use `(10)` and the mean package-cost theorem of `MC-372`. Without quartic saturation, the frame bound gives only the lower-conductor scarcity statements `(3)`, `(7)`, and `(9)`.
- **No RH or Mertens consequence.** The result concerns realizability and source complexity of the endpoint character family. It does not yield a zero-free region for `\zeta`, an RH implication, or a bound for `M(x)`.

## Consequence for the research line

The minimum-primitive-conductor ambiguity left by `MC-372` is now resolved in density at the current analytic frontier. Under quartic source saturation, almost every middle-layer mode has both package cost and true primitive conductor `y^{2+o(1)}`. There is no large hidden population of cheaply re-encoded central modes waiting to force endpoint defect balance.

This sharply narrows the next analytic interface. The middle endpoint layer sits genuinely at the quadratic primitive-conductor boundary, while `MC-373` shows that the present Burgess/Halász--Montgomery technology approaches that boundary only from below. Progress must therefore extract additional structure at conductor `y^{2+o(1)}`, strengthen the prime-character exponent, or use information not captured by the positive frame/energy architecture.