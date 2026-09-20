# PL-395 — Restoring the Riemann–Siegel moving cutoff collapses the cross-channel stationary shell to a diagonal boundary resonance

**Evidence/status:** `CLASSICAL-RIEMANN-SIEGEL+EXACT-DERIVED + REPRESENTATION-QUOTIENT + ROUTE-RESTRICTION/PRIOR-ART-REDIRECT`.

**Parent finding:** `PL-394`.

## Claim

`PL-394` identified the phase

\[
\Phi_{n,m}(t)=2\theta(t)-t\log(nm)
\]

in the functional-equation cross channel and, while explicitly suppressing the moving-cutoff bookkeeping, observed the stationary shell

\[
nm\asymp \frac{t}{2\pi}.
\]

Restoring the **actual balanced Riemann–Siegel cutoff** changes the geometry sharply. Let

\[
M(t)=\left\lfloor\sqrt{\frac{t}{2\pi}}\right\rfloor,
\qquad
A(t)=\sum_{n\le M(t)}n^{-1/2-it}.
\]

The cross channel in the leading approximation to `|zeta(1/2+it)|^2` (equivalently in the square of Hardy's real `Z`-function after phase rotation) contains

\[
e^{2i\theta(t)}A(t)^2
=
\sum_{n,m\le M(t)}
\frac{e^{i\Phi_{n,m}(t)}}{\sqrt{nm}}.
\]

A fixed pair `(n,m)` is present only when

\[
t\ge t_{\rm on}(n,m)
:=2\pi\max(n,m)^2.
\]

On the other hand, Stirling's expansion gives

\[
2\theta'(t)
=
\log\frac{t}{2\pi}
-\frac{1}{24t^2}
+O(t^{-4}),
\]

so a stationary point of that pair would satisfy

\[
\Phi'_{n,m}(t)=0
\quad\Longrightarrow\quad
 t_{n,m}=2\pi nm+O((nm)^{-1}).
\]

If `n != m`, write `q=max(n,m)` and `r=min(n,m)`. Then

\[
t_{\rm on}-2\pi nm
=2\pi q(q-r)
\ge 2\pi q,
\]

whereas the Stirling displacement of the stationary point is only `O((nm)^(-1))`. Equivalently, at activation,

\[
\Phi'_{n,m}(2\pi q^2)
=
\log\frac qr+O(q^{-4})>0
\]

for all sufficiently large off-diagonal pairs, and `Phi'` is increasing thereafter. Thus **the off-diagonal stationary point occurs before the pair has entered the moving Riemann–Siegel sum**.

For `n=m`, by contrast, the nominal saddle `2 pi n^2` coincides with the activation boundary. The first Stirling correction moves the true saddle only `O(n^(-2))` to the active side. Therefore the moving-cutoff cross channel has the asymptotic stationary geometry

\[
\boxed{
\text{active stationary pairs} \;\Longrightarrow\; n=m,
\qquad
 t\approx 2\pi n^2.
}
\]

In prime-exponent coordinates the broad sum-energy shell from `PL-394` therefore intersects the actual moving support, at stationary phase, only on

\[
\boxed{
(v(n),v(m))=(\alpha,\alpha),
\qquad
v(n)+v(m)=2\alpha,
}
\]

that is, on the diagonal of the pair lattice and the perfect-square/even sublattice after multiplication.

This is a **route restriction, not an RH mechanism**. It closes the moving-cutoff caveat left explicit in `PL-394`: the canonical quadratic cross channel does not provide a broad stationary two-body shell once its true support is restored. Off-diagonal arithmetic can still survive through cutoff-activation/end-point terms, especially in a near-diagonal layer, but not through interior stationary points of the active pair phases.

## 1. The support condition is exact

The balanced approximate functional equation on the critical line uses

\[
M(t)=\left\lfloor\sqrt{t/(2\pi)}\right\rfloor.
\]

For a fixed pair `(n,m)`, both summands occur exactly when

\[
M(t)\ge \max(n,m)=q.
\]

Since `q` is an integer, this is equivalent to

\[
\sqrt{t/(2\pi)}\ge q,
\]

hence to

\[
\boxed{t\ge 2\pi q^2.}
\]

No asymptotic estimate or continuation argument enters this support boundary. It is a finite statement about the Riemann–Siegel truncation.

## 2. The stationary center lies before activation off the diagonal

For real `t`, the Riemann–Siegel phase is

\[
\theta(t)
=
\operatorname{Im}\log\Gamma\!\left(\frac14+\frac{it}{2}\right)
-\frac t2\log\pi.
\]

Differentiating the standard Stirling expansion gives

\[
\theta'(t)
=
\frac12\log\frac{t}{2\pi}
-\frac{1}{48t^2}
+O(t^{-4}),
\]

and therefore

\[
\Phi'_{n,m}(t)
=
\log\frac{t}{2\pi nm}
-\frac{1}{24t^2}
+O(t^{-4}).
\tag{1}
\]

For large `t`,

\[
\Phi''_{n,m}(t)=\frac1t+O(t^{-3})>0,
\]

so there is at most one high-energy stationary point. Solving (1) perturbatively yields

\[
t_{n,m}=2\pi nm+O((nm)^{-1}).
\tag{2}
\]

Suppose `q=max(n,m)>r=min(n,m)`. The pair turns on at `2 pi q^2`, while its nominal saddle is at `2 pi qr`. Their separation is

\[
2\pi q^2-2\pi qr
=2\pi q(q-r),
\]

which is at least `2 pi q`. The correction in (2) is negligible compared with this gap. A local way to see the same fact is to evaluate (1) at the exact activation boundary:

\[
\Phi'_{n,m}(2\pi q^2)
=
\log(q/r)+O(q^{-4}).
\]

Even for the closest pair `r=q-1`, the main term is of order `1/q`, much larger than the `O(q^(-4))` correction. Hence it is positive for all sufficiently large off-diagonal pairs; monotonicity then keeps it positive for every later `t` where the pair is active.

If `n=m`, the two scales coincide. At `t_0=2 pi n^2`, equation (1) gives

\[
\Phi'_{n,n}(t_0)
=-\frac{1}{24t_0^2}+O(t_0^{-4})<0,
\]

while `Phi''>0`. The unique zero therefore lies just to the active side,

\[
t_{n,n}=2\pi n^2+O(n^{-2}).
\]

Thus the surviving saddle is a **boundary saddle born with the diagonal term**, not an interior shell populated by generic factor pairs.

## 3. The quadratic pair lattice also factors through the product quotient

There is a second exact way to see how little independent pair geometry remains after scalar summation. For a frozen integer cutoff `M`,

\[
A_M(t)=\sum_{n\le M}n^{-1/2-it}
\]

satisfies the finite identity

\[
A_M(t)^2
=
\sum_{k\le M^2}
\frac{d_M(k)}{\sqrt{k}}e^{-it\log k},
\tag{3}
\]

where

\[
d_M(k)
=
\#\{d\mid k:\ d\le M,\ k/d\le M\}
=
\#\{d\mid k:\ k/M\le d\le M\}.
\tag{4}
\]

In exponent coordinates this is the map

\[
Q:(\alpha,\beta)\longmapsto \alpha+\beta.
\]

By the representation taxonomy, `Q` is a **many-to-one quotient/compression**, not a faithful change of coordinates. It preserves

\[
\langle\alpha+\beta,(\log p)_p\rangle
=\log(nm)
\]

and the total fiber multiplicity `d_M(k)`, but loses the ordered factor labels and all pair information not recoverable from the sum exponent plus that multiplicity.

For the moving cutoff `M=M(t)`, the stationary condition from `PL-394` is `k approx t/(2 pi)`, while the support in (3) ends at

\[
M(t)^2\le \frac{t}{2\pi}.
\]

So the nominal stationary shell sits at the **upper product boundary** of the quotient polynomial. The pair-level calculation above refines this further: at an actual active saddle, that boundary fiber asymptotically reduces to the square `k=n^2` and the diagonal factorization `(n,n)`.

Equation (3) is a finite algebraic identity and is valid for every real or complex `t`; it uses no Euler-product continuation. In the untruncated half-plane `Re(s)>1`, the analogous coefficient convolution gives the classical identity `zeta(s)^2=sum d(k)k^(-s)`, but no use of that infinite Dirichlet series outside its convergence half-plane is needed here.

## 4. Prior-art and novelty audit

No theorem-level novelty in classical analytic number theory is claimed.

The balanced approximate functional equation, Hardy `Z`-function and Riemann–Siegel formula are classical. DLMF §25.9 records the two-piece Titchmarsh approximate functional equation and the cutoff `floor sqrt(t/(2 pi))`; DLMF §25.10 records

\[
Z(t)=e^{i\theta(t)}\zeta(1/2+it)
\]

and the Riemann–Siegel cosine sum with exactly that moving cutoff. The phase asymptotic follows from standard Stirling expansion of `Gamma`. Stationary-phase treatments of Riemann–Siegel sums are classical, and mean-square analysis of the critical-line zeta function leads into the classical Atkinson/divisor-sum theory. F. V. Atkinson's 1949 formula and later expositions by Ivić are explicit prior-art controls against treating oscillatory divisor structures obtained from quadratic zeta statistics as new.

The factorization (3) is just finite Dirichlet convolution and is not claimed as new. A targeted literature search for Riemann–Siegel stationary phase, zeta mean-square cross terms and Atkinson's formula found a large classical literature on precisely these oscillatory/divisor mechanisms. A targeted local audit found `PL-394` as the relevant immediate predecessor; its Section 3 deliberately suppressed moving-cutoff bookkeeping and its adversarial boundary 2 explicitly left moving-cutoff statistics outside the proved route restriction.

The durable delta here is therefore **line-specific bookkeeping closure**: once the exact cutoff from the same classical Riemann–Siegel formula is restored, the broad pair-lattice stationary shell used diagnostically in `PL-394` is not available as an active interior saddle. It meets the moving support only on the diagonal boundary at leading stationary phase. This narrows, rather than extends, the classical theory.

### Sources

1. NIST Digital Library of Mathematical Functions, §25.9, “Asymptotic Approximations” for the Riemann zeta function, especially equations 25.9.1--25.9.3: https://dlmf.nist.gov/25.9. Source there: E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., revised by D. R. Heath-Brown, Oxford University Press, 1986, §§4.11--4.18.
2. NIST Digital Library of Mathematical Functions, §25.10, “Zeros,” especially equations 25.10.1--25.10.4 defining Hardy's `Z`-function and the Riemann–Siegel formula: https://dlmf.nist.gov/25.10. Source there: Titchmarsh, §4.17.
3. NIST Digital Library of Mathematical Functions, §5.11, “Asymptotic Expansions” for `Gamma` and digamma: https://dlmf.nist.gov/5.11.
4. F. V. Atkinson, “The mean value of the Riemann zeta-function,” *Acta Mathematica* **81** (1949), 353--376. DOI: https://doi.org/10.1007/BF02395027.
5. A. Ivić, *The Riemann Zeta-Function: Theory and Applications*, Wiley, 1985; Dover reprint, 2003, especially the chapters on approximate functional equations, the divisor problem and Atkinson's formula.

## 5. Adversarial boundaries

1. **This does not diagonalize the full cross channel.** It diagonalizes only its high-energy **interior stationary points after the moving support is imposed**. Off-diagonal terms remain present and can contribute by ordinary nonstationary integration, by the discontinuous activation boundary, or through a smoothed cutoff's transition layer.

2. **Near-diagonal endpoint terms are a genuine surviving channel.** For `q-r` small,

\[
\Phi'_{r,q}(2\pi q^2)\sim \log(q/r)\sim (q-r)/q,
\]

so the phase can be slow exactly when an off-diagonal term turns on. The present result therefore redirects attention from a bulk stationary shell to a moving near-diagonal **boundary layer**; it does not prove that this layer is negligible.

3. **The product map is a quotient only after scalar pair summation.** An operator-valued construction that keeps `(n,m)` as separate labels need not factor through `v(n)+v(m)`. The finding rules out assigning extra geometry to the already-summed quadratic scalar cross term, not every two-body prime-lattice construction.

4. **Hardy's `Z`-function is not an RH proof.** For real `t`, its zeros are exactly critical-line zeta zeros, with multiplicity, but showing that these exhaust the full nontrivial zero count is the RH difficulty. Sign changes detect odd-multiplicity real zeros and must not be conflated with a multiplicity-sensitive zero count.

5. **The Riemann–Siegel main sum is asymptotic, not the exact zeta function.** Near a zero, the remainder can affect the location of zeros of a truncated cosine sum. The exact object is `Z(t)=e^{i theta(t)} zeta(1/2+it)`; the finite sum plus remainder is its classical high-height representation.

6. **The saddle exclusion is asymptotic.** The argument using Stirling applies to sufficiently large pairs. Finitely many low-height exceptions would not affect RH, but the statement is not advertised as a finite-`t` classification without direct checking.

7. **No formal Euler-product continuation is used.** All critical-strip information enters through the proven approximate functional equation/Riemann–Siegel representation; the product-quotient identity is finite.

## Research consequence

The post-`PL-394` frontier can be narrowed again. It is not enough to say that a continuation-faithful quadratic statistic retains the reflected packet and has a stationary condition

\[
\langle v(n)+v(m),(\log p)_p\rangle\approx\log(t/(2\pi)).
\]

With the canonical moving cutoff, generic off-diagonal points satisfying that condition would have reached their saddle **before they are admitted to the sum**. The active stationary locus is instead the diagonal/perfect-square boundary

\[
(v(n),v(n)),\qquad t\approx2\pi n^2.
\]

Consequently, future work should not treat the broad sum-energy shell itself as unexplored prime-lattice geometry. A genuinely new mechanism would need to exploit what survives this collapse: the near-diagonal cutoff-activation layer, an observable that keeps factor labels instead of quotienting by `(alpha,beta)->alpha+beta`, a nonquadratic interaction, or a global/argument-principle coupling that is sensitive to whether critical-line zeros saturate the total zero count. Any such proposal still has to beat the matched-control and individual-zero-sensitivity gates from `PL-391`--`PL-394`.