# WP-204 — Smooth Gamma-resolvent calculus is too smooth for the reciprocal floor

**Status:** `DERIVED + EXACT + ARCHIMEDEAN-GAMMA-RESOLVENT + HIGHER-ORDER-SPECTRAL-SHIFT + SMOOTH-FUNCTIONAL-CALCULUS-NO-GO + SHARP-POWER-CONTROL + SOURCE-FORCING-NARROWING + PRIOR-ART-AUDITED + NOT-A-WEIL-BRIDGE`.

`WP-203` shows that the exact Riemann Gamma relative determinant can coexist with centered inverse-power baths on opposite sides of the `WP-202` reciprocal-floor boundary. It therefore leaves a natural source-forcing question: perhaps the determinant does not select a fractional power globally, but its **local differential geometry** in the shift parameter does.

For the canonical Gamma number operator, that route fails in a precise way. Every finite smooth compact functional calculus of its inverse resolvent is too regular at spectral zero. More generally, if the compact channel vanishes like `x^alpha` with

\[
\alpha>\frac1{n-1},
\qquad n=4k\ge4,
\]

then it lies in `S^{n-1}` and cannot have the reciprocal Fourier floor required by `WP-202`. In particular every `C^1` compact calculus, every finite determinant jet, and every finite smooth matrix/Gram construction from those jet channels fails.

The boundary is sharp inside the power family: the successful `WP-203` channel is

\[
x\longmapsto x^{1/(n-1)},
\]

which is deliberately **not** `C^1` at zero. Thus the sign-producing reservoir cannot come from ordinary finite smooth variation of the Gamma determinant. It requires a genuinely fractional/singular spectral operation, infinite or nonlocal structure, or coupling that mixes spectral levels or finite primes before the sign theorem is applied.

This is a source-forcing obstruction only. It does not rule out a geometric principle that independently forces the critical fractional calculus, and it does not produce the finite Mangoldt or polar terms required by the global Weil form.

## 1. A Hölder-decay obstruction for the Gamma inverse resolvent

Use the canonical operator from `WP-203`,

\[
D_a=N+a,
\qquad
L_a=\frac{D_a}{\pi},
\qquad
R_a=L_a^{-1}=\pi D_a^{-1},
\qquad a>0.
\tag{1}
\]

On the number basis,

\[
R_a e_j=r_j e_j,
\qquad
r_j=\frac{\pi}{j+a}.
\tag{2}
\]

Allow a finite channel fibre `C^d`. Let

\[
\Phi:[0,r_0]\to M_d(\mathbb C)
\]

be continuous near zero, positive semidefinite, with `Phi(0)=0`, and define the centered positive bath

\[
V_\Phi
=
\bigoplus_{j\ge0}\Phi(r_j)
\quad\text{on}\quad
\ell^2(\mathbb N_0)\otimes\mathbb C^d.
\tag{3}
\]

Suppose that for some

\[
\alpha>\frac1{n-1}
\tag{4}
\]

there are `C,epsilon>0` such that

\[
\|\Phi(x)\|\le Cx^\alpha
\qquad(0\le x\le\epsilon).
\tag{5}
\]

For all sufficiently large `j`, every singular value of the `j`th fibre is at most `C r_j^alpha`. Hence

\[
\begin{aligned}
\|V_\Phi\|_{\mathcal S^{n-1}}^{n-1}
&=
\sum_j \operatorname{Tr}\!\left(\Phi(r_j)^{n-1}\right)\\
&\le
C_0+
 dC^{n-1}\sum_{j\gg1}r_j^{\alpha(n-1)}\\
&<\infty,
\end{aligned}
\tag{6}
\]

because `alpha(n-1)>1`. Therefore

\[
\boxed{
V_\Phi\in\mathcal S^{n-1}\subset\mathcal S^n.
}
\tag{7}
\]

`WP-198` proves that a centered `S^{n-1}` bath cannot universally absorb even one fixed off-zero scalar positive source. Equivalently, by the necessary-and-sufficient classification of `WP-202`, its even higher-order spectral-shift multiplier cannot satisfy

\[
\liminf_{|\xi|\to\infty}|\xi|F_\Phi(\xi)>0.
\tag{8}
\]

Thus (5) is an exact no-go criterion for this architecture.

A particularly useful corollary is immediate. If `Phi` is `C^1` at zero and `Phi(0)=0`, then finite-dimensional differentiability gives

\[
\|\Phi(x)\|=O(x),
\tag{9}
\]

and `1>1/(n-1)` for every `n>=4`. Hence **every `C^1` compact positive functional calculus of `R_a` fails the reciprocal-floor gate**.

There is also no escape through a nonzero smooth constant term. If `Phi(0) != 0`, then the blocks `Phi(r_j)` converge to a nonzero matrix and `V_Phi` is not compact, hence is not in the required `S^n` higher-order perturbation category at all. Smooth finite-fibre calculi therefore have a dichotomy:

\[
\boxed{
\Phi(0)\ne0\Rightarrow V_\Phi\notin\mathcal S^n,
\qquad
\Phi(0)=0,\ \Phi\in C^1\Rightarrow V_\Phi\in\mathcal S^{n-1}.
}
\tag{10}
\]

Neither side can supply the `WP-202` resource.

## 2. Finite Gamma-determinant jets lie inside the smooth no-go class

The exact relative determinant from `WP-203` is

\[
\frac{\det_\zeta L_a}{\det_\zeta L_{a+z}}
=
\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}.
\tag{11}
\]

Before taking the regularized trace, the shift derivatives of the spectral logarithm are completely rigid. Since each eigenvalue of `L_q` is `(j+q)/pi`,

\[
\boxed{
\frac{\partial^m}{\partial q^m}\log L_q
=
(-1)^{m-1}(m-1)!\,D_q^{-m},
\qquad m\ge1.
}
\tag{12}
\]

Thus the operator-level finite differential jet at `q=a` consists only of the integer resolvent powers

\[
D_a^{-1},D_a^{-2},\ldots,D_a^{-m},
\tag{13}
\]

or equivalently integer powers of `R_a` up to fixed factors of `pi`.

The scalar determinant derivatives show the same structure. From (11), for `m>=2`,

\[
\frac{d^m}{dz^m}
\log\!\left(
\frac{\det_\zeta L_a}{\det_\zeta L_{a+z}}
\right)_{z=0}
=
\psi^{(m-1)}(a)
=
(-1)^m(m-1)!\zeta(m,a),
\tag{14}
\]

and

\[
\zeta(m,a)=\operatorname{Tr}D_a^{-m}.
\tag{15}
\]

The first derivative is the usual regularized resolvent trace `-log pi + psi(a)`; its underlying operator channel is still `D_a^{-1}`. The polygamma identities in (14) are classical.

Consequently any finite construction that takes finitely many channels (13), applies fixed finite-dimensional matrix mixing and a smooth map vanishing at the zero tuple, and then forms finite sums, products, direct sums, or positive Grams has high-mode norm

\[
O(r_j).
\tag{16}
\]

Products and Grams only improve the decay. Such a construction is a special case of (9) and therefore belongs to `S^{n-1}`.

Hence

\[
\boxed{
\text{finite smooth differential geometry of the Gamma determinant}
\not\Rightarrow
\text{the reciprocal-floor bath.}
}
\tag{17}
\]

The obstruction is not that the finite jet forgets the Gamma function: equations (11)--(15) are exactly its canonical shift variation. The obstruction is that ordinary differential variation produces **integer resolvent powers**, while the sign resource lives at a much rougher fractional spectral boundary.

## 3. The critical fractional root is exactly outside the smooth class

Take the scalar power calculus

\[
\Phi_\beta(x)=x^\beta.
\tag{18}
\]

Then

\[
V_{\Phi_\beta}=R_a^\beta
\]

has singular values asymptotic to `j^{-beta}`. The general estimate above gives

\[
\beta>\frac1{n-1}
\quad\Longrightarrow\quad
V_{\Phi_\beta}\in\mathcal S^{n-1},
\tag{19}
\]

which recovers the smooth side of the exact power-law threshold in `WP-200` and `WP-203`.

At the endpoint

\[
\beta_c=\frac1{n-1},
\tag{20}
\]

`WP-203` computes explicitly

\[
\lim_{\xi\to\infty}
\xi F_{a,\beta_c}(\xi)
=
\frac{\pi^2}{2(n-2)!}>0.
\tag{21}
\]

But because `n>=4`, `beta_c<1`, so

\[
\Phi_{\beta_c}'(x)
=\beta_c x^{\beta_c-1}
\longrightarrow\infty
\qquad(x\downarrow0).
\tag{22}
\]

The exact sign-producing endpoint is therefore a **singular fractional root at the accumulation point of the Gamma resolvent spectrum**. It cannot be obtained from a finite `C^1` jet calculus.

This distinction survives exact Gamma normalization. `WP-203` shows that one may combine the critical exponent `1/(n-1)` with complementary fractional channels whose exponents sum to one and thereby keep the exact relative determinant (11). What (11) does not do is force the singular root. The finite differential jet does not force it either.

The boundary in (4) is sharp for powers, but it is not a complete characterization for arbitrary spectra. At the borderline, distribution across scales matters: `WP-201` gives lacunary rough baths with Fourier valleys, while `WP-202` says the true criterion is the uniform reciprocal floor itself. Thus this finding does not replace the `WP-202` classification with a Hölder exponent criterion.

## 4. Aggressive falsification and exact scope

**Can finite-rank low-mode corrections repair a smooth Gamma bath?** No. Finite-rank perturbations preserve `S^{n-1}` membership, so the source-variation obstruction remains. They can modify bounded-frequency behavior but cannot manufacture the uniform reciprocal high-frequency floor.

**Can a finite matrix of smooth channels evade the scalar estimate?** No. Equation (6) already allows arbitrary fixed finite fibre dimension and positive matrix-valued `Phi`. After blockwise diagonalization it is still a centered compact positive bath, and the same Schatten estimate applies.

**Does non-`C^1` automatically succeed?** No. Failure of smoothness is only necessary for this route, not sufficient. A function can be non-Lipschitz at zero and still generate an `S^{n-1}` bath, and even `S^n\setminus S^{n-1}` does not by itself imply the reciprocal floor; `WP-201` is the matched counterexample.

**Could an intrinsic fractional geometric operator evade the result?** Yes. A Dirichlet-to-Neumann square root, fractional Laplacian, extension problem, or other geometry might independently produce a singular power. Such a mechanism would be genuine additional structure and must be audited on its own. This finding rules out claiming that the critical fractional operation follows merely from the finite smooth shift geometry of the Gamma determinant.

**Could mixing different number levels evade the result?** Yes. Equation (3) is a functional calculus of the canonical Gamma resolvent and therefore preserves its spectral fibres. Non-diagonal cross-level coupling, an infinite channel fibre, a singular domain change, or a finite--archimedean coupling formed before diagonalization lies outside the theorem.

**Does the result depend on the Riemann shift `a=1/4`?** No. The estimate uses only `r_j~pi/j` and holds for every `a>0`. This gives an immediate non-Riemann matched control: the smoothness obstruction does not distinguish the Riemann Gamma shift.

**What about the positive digamma jump geometry of `WP-117`?** That is a different construction. `WP-117` extracts a conditionally negative-definite critical-line Gamma variation and proves a Markov/Dirichlet positivity theorem; it then fails under direct critical prime coupling. The present result concerns the later higher-order spectral-shift reservoir architecture and asks whether the Gamma determinant itself can source-force its required high-frequency floor.

## 5. Prior art and novelty boundary

No novelty is claimed for zeta-regularized determinants, the Hurwitz zeta/Gamma identity, polygamma functions, fractional functional calculus, or Schatten ideals.

The determinant identity in (11) is the classical Hurwitz-zeta calculation already audited in `WP-203` using NIST DLMF §25.11. The derivative identity in (14) is the standard polygamma/Hurwitz-zeta relation; NIST DLMF §5.15 records the polygamma functions and their inverse-power series, in particular `psi'(z)=sum_{k>=0}(k+z)^{-2}` with the higher derivatives obtained by differentiation. Vardi's *Determinants of Laplacians and Multiple Gamma Functions* (SIAM J. Math. Anal. 19 (1988), DOI `10.1137/0519035`) is a classical spectral-determinant/Gamma comparison point.

The Schatten estimate (6) is elementary for the explicit diagonal spectrum (2). The implication from `S^{n-1}` to failure of universal positive stabilization is internal to this research line (`WP-198`, sharpened to the reciprocal-floor criterion in `WP-202`).

A targeted literature search across Gamma/Hurwitz spectral determinants, polygamma variation, fractional powers, and Schatten functional calculus found the classical ingredients but no prior statement of the Mathia-specific consequence (17). No historical novelty is inferred from that absence. The durable delta is the exact source-forcing boundary: **ordinary finite smooth determinant variation cannot generate the singular spectral roughness demanded by the independently derived `WP-202` Weil-cone gate**.

## 6. Consequence for `weil_positivity`

`WP-203` showed that exact Gamma determinant provenance does not choose the sign-producing fractional split. This finding closes the most immediate attempt to recover that choice from local differential information: every finite smooth Gamma-resolvent jet remains on the `S^{n-1}` side of the boundary.

The architecture is therefore forced into a sharper category change. If the reciprocal-floor route is to remain relevant, the Riemann source must intrinsically provide at least one of:

- a singular/fractional functional calculus at the zero accumulation point of the Gamma resolvent;
- infinite or nonlocal structure not reducible to a finite smooth determinant jet;
- non-diagonal spectral mixing; or
- a nonseparable finite--archimedean/global coupling formed before the positivity theorem.

Merely differentiating, linearly mixing, or taking finite positive Grams of the canonical Gamma determinant data cannot do the job.

Even a successful source-forced fractional real-place reservoir would still not answer the branch mandate by itself. The same completed object must generate the signed finite Mangoldt structure and the pole/global counterterms and prove the assembled Weil-type sign independently of RH or inserted zero data. `WP-199`--`WP-203` remain matched-control laboratories until such a coupling is derived.

## Dependencies

- `research/weil_positivity/findings/WP-117-riemann-gamma-digamma-variation-is-markov-positive-but-critical-prime-coupling-diverges.md`
- `research/weil_positivity/findings/WP-198-rough-infinite-centered-bath-defeats-finite-positive-source-4k-no-go.md`
- `research/weil_positivity/findings/WP-200-power-law-centered-baths-have-a-sharp-source-variation-stabilization-threshold.md`
- `research/weil_positivity/findings/WP-201-lacunary-rough-baths-have-fourier-valleys-and-fail-universal-stabilization.md`
- `research/weil_positivity/findings/WP-202-universal-centered-bath-stabilization-is-equivalent-to-a-reciprocal-fourier-floor.md`
- `research/weil_positivity/findings/WP-203-exact-gamma-determinant-does-not-fix-the-reciprocal-floor-geometry.md`

## Bottom line

For the canonical Gamma inverse resolvent `R_a`, every finite positive matrix functional calculus satisfying

\[
\|\Phi(x)\|=O(x^\alpha),
\qquad
\alpha>\frac1{n-1},
\]

lies in `S^{n-1}` and therefore fails the exact `WP-202` reciprocal-floor gate. Every compact `C^1` calculus and every finite smooth determinant-jet construction is in this class. The power-law channel that reaches the gate sits exactly at the singular fractional exponent `1/(n-1)` and is not `C^1` at spectral zero.

So the Gamma determinant's ordinary smooth local geometry does not source-force the higher-order positivity resource. Any surviving explanation must derive a genuinely singular/nonlocal operation or a stronger mixed finite--archimedean geometry rather than insert the critical fractional root by hand.