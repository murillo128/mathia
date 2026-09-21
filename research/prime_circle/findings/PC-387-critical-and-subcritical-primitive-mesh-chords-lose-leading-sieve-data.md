# PC-387 — critical and subcritical primitive mesh chords lose leading sieve data

**Status:** `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the critical/subcritical exact-order primitive restriction left open by PC-386.

PC-386 shows that common-anchor inverse-chord powers on the primitive `m`-shell retain an explicit coprimality sieve at mesh scale when `alpha>1/2`. The remaining question is whether the critical or integrable singularity range `alpha<=1/2` preserves a comparable leading arithmetic signal. It does not. The threshold `alpha=1/2` is exactly the transition: below it, the primitive average converges to the same continuum integral for every degree sequence; at the threshold, the leading divergence is universally `phi(m) log m / pi`. At zero cutoff the first arithmetic correction can be computed explicitly, but it is only the logarithmic derivative at `s=1` of the finite Euler product attached to the radical of `m`.

This completes the scalar primitive-shell mesh branch of PC-386. It is a useful prime-circle boundary theorem, not a new RH mechanism: the supercritical side retains only the classical coprimality sieve, while the critical/subcritical side loses that sieve at leading order and leaves at most elementary finite-Euler-product data below it.

## 1. Setup

For `alpha>=0` and `tau>=0`, put

\[
S_m\!\left(\alpha,\frac{\tau}{m}\right)
:=\sum_{\substack{1\le a<m\\(a,m)=1}}
\left[2\left(\cosh\frac{\tau}{m}-\cos\frac{2\pi a}{m}\right)\right]^{-\alpha}.
\tag{1}
\]

The identity

\[
2\left(\cosh\frac{\tau}{m}-\cos\frac{2\pi a}{m}\right)
=4\left[\sinh^2\!\left(\frac{\tau}{2m}\right)+\sin^2\!\left(\frac{\pi a}{m}\right)\right]
\tag{2}
\]

shows that fixed `tau` is precisely a mesh-scale regularization of the endpoint singularity. At `tau=0`, exact-order extraction is the elementary Möbius identity

\[
S_m(\alpha,0)
=\sum_{d\mid m}\mu(d)\,C_{m/d}(\alpha),
\qquad
C_q(\alpha):=\sum_{a=1}^{q-1}[4\sin^2(\pi a/q)]^{-\alpha}.
\tag{3}
\]

Thus any arithmetic surviving in this scalar observable must come from how Möbius extraction interacts with the endpoint asymptotics of the full-root sum.

## 2. Subcritical regime: the primitive average is universal

Let `0<=alpha<1/2`. Then the continuum kernel is integrable and

\[
I_\alpha
:=\int_0^1[4\sin^2(\pi x)]^{-\alpha}\,dx
=\frac{2^{-2\alpha}}{\sqrt\pi}
\frac{\Gamma(\tfrac12-\alpha)}{\Gamma(1-\alpha)}.
\tag{4}
\]

For `0<alpha<1/2`, monotone comparison on the two endpoint halves gives the full-shell estimate

\[
C_q(\alpha)=qI_\alpha+O_\alpha(q^{2\alpha}).
\tag{5}
\]

Substituting (5) into (3),

\[
S_m(\alpha,0)
=\varphi(m)I_\alpha
+O_\alpha\!\left(
 m^{2\alpha}\prod_{p\mid m}(1+p^{-2\alpha})
\right).
\tag{6}
\]

Because `2^{omega(m)}=m^{o(1)}` and `m/phi(m)=m^{o(1)}`, the error in (6) is `o(phi(m))` for every fixed `alpha<1/2`. The endpoint `alpha=0` is exact, since the sum is simply `phi(m)`. Hence, with no restriction on the prime divisors of the degree sequence,

\[
\boxed{
\frac{S_m(\alpha,0)}{\varphi(m)}\longrightarrow I_\alpha,
\qquad 0\le\alpha<\tfrac12.
}
\tag{7}
\]

Fixed mesh regularization does not change the limit. From (2), the total difference between the `tau/m` and zero-cutoff full-shell sums is `O_{alpha,tau}(m^{2 alpha})`; the primitive sum is a positive subsum of that difference. Dividing by `phi(m)` therefore gives

\[
\boxed{
\frac{S_m(\alpha,\tau/m)}{\varphi(m)}\longrightarrow I_\alpha
\quad\text{for every fixed }\tau\ge0,
\qquad 0\le\alpha<\tfrac12.
}
\tag{8}
\]

Unlike the supercritical law in PC-386, there is no subsequential radical dependence at leading order. The primitive mask has become asymptotically invisible after averaging.

## 3. Critical regime: universal logarithmic growth

At `alpha=1/2` and zero cutoff,

\[
S_m(\tfrac12,0)
=\frac12
\sum_{\substack{1\le a<m\\(a,m)=1}}
\csc\!\left(\frac{\pi a}{m}\right).
\tag{9}
\]

Let

\[
C_q:=\sum_{a=1}^{q-1}\csc(\pi a/q).
\tag{10}
\]

The classical cosecant-sum asymptotic, in a form with enough remainder for divisor inversion, is

\[
C_q
=\frac{2q}{\pi}\left(\log\frac{2q}{\pi}+\gamma\right)
+O(q^{-1}).
\tag{11}
\]

Blagouchine--Moreau give complete asymptotic expansions and sharp bounds for this full sum. Möbius extraction of the reduced residue classes gives

\[
2S_m(\tfrac12,0)=\sum_{d\mid m}\mu(d)C_{m/d}.
\tag{12}
\]

Using

\[
\sum_{d\mid m}\frac{\mu(d)}d=\frac{\varphi(m)}m
\tag{13}
\]

and differentiating the finite Euler product

\[
F_m(s):=\sum_{d\mid m}\frac{\mu(d)}{d^s}
=\prod_{p\mid m}(1-p^{-s}),
\tag{14}
\]

at `s=1`, one obtains

\[
-\sum_{d\mid m}\frac{\mu(d)\log d}{d}
=\frac{\varphi(m)}m
\sum_{p\mid m}\frac{\log p}{p-1}.
\tag{15}
\]

The `O(q^{-1})` remainder in (11), with the harmless `q=1` endpoint absorbed into a bounded remainder, contributes at most

\[
O\!\left(\frac1m\sum_{d\mid\operatorname{rad}(m)}d\right)
=O\!\left(\prod_{p\mid m}(1+p^{-1})\right)
=O\!\left(\frac{m}{\varphi(m)}\right).
\tag{16}
\]

Therefore

\[
\boxed{
S_m(\tfrac12,0)
=\frac{\varphi(m)}{\pi}
\left[
\log m+\gamma+\log\frac{2}{\pi}
+\sum_{p\mid m}\frac{\log p}{p-1}
\right]
+O\!\left(\frac{m}{\varphi(m)}\right).
}
\tag{17}
\]

In particular,

\[
\boxed{
\frac{S_m(\tfrac12,0)}{\varphi(m)\log m}\longrightarrow\frac1\pi.
}
\tag{18}
\]

The arithmetic term in (17) can grow, for example on primorial-like sequences, but it is lower order than `log m`. More importantly, it is exactly

\[
\boxed{
\sum_{p\mid m}\frac{\log p}{p-1}
=\left.\frac{d}{ds}\log\prod_{p\mid m}(1-p^{-s})\right|_{s=1}.
}
\tag{19}
\]

So the first explicit radical-dependent correction is not a new spectral object: it is the logarithmic derivative of a finite Euler product evaluated at the classical boundary point `s=1`.

For fixed `tau>0`, comparison of (2) with the zero-cutoff kernel gives a total difference `O_tau(m)` at `alpha=1/2`. Since `m/phi(m)=O(log log m)`, this is `o(phi(m) log m)`. Thus the leading critical law is unchanged:

\[
\boxed{
\frac{S_m(\tfrac12,\tau/m)}{\varphi(m)\log m}
\longrightarrow\frac1\pi
\quad\text{for every fixed }\tau\ge0.
}
\tag{20}
\]

Equation (17) is asserted only at `tau=0`; fixed nonzero mesh regularization may change lower-order terms while leaving (20) intact.

## 4. The scalar primitive phase diagram is now complete

Together with PC-386, equations (8) and (20) give a sharp information transition at `alpha=1/2`.

- For `alpha>1/2`, the mesh-scale boundary layer is summable and the leading normalized primitive observable retains the coprimality sieve, equivalently positive-real zeta values with finite Euler factors at zero cutoff.
- For `alpha=1/2`, the endpoint harmonic divergence overwhelms that leading sieve dependence. The main term is universally `phi(m) log m / pi`; at zero cutoff the first explicit arithmetic correction is the finite Euler-product derivative (19).
- For `0<=alpha<1/2`, the singularity is integrable and even the primitive average has the universal continuum limit (8), independent of the radical of `m`.

This rules out the remaining scalar inverse-chord-power mesh branch as a source of a new RH mechanism. Below the threshold there is no leading arithmetic signal to organize; at the threshold the surviving lower-order arithmetic is finite-Euler-product data at `s=1`; above it PC-386 already identifies the signal as the classical coprimality sieve. None of the three regimes supplies a free complex spectral parameter, a completed-zeta functional equation, or an intrinsic selector for `Re(s)=1/2`.

The conclusion is deliberately limited to these scalar primitive-shell common-anchor energies. It does not rule out cross-level, phase-sensitive, tensorial, nonnormal, or other genuinely nonseparable constructions that retain information before scalar summation.

## 5. Novelty audit

The ingredients are classical: endpoint-singularity Riemann-sum asymptotics, Möbius extraction of reduced residue classes, and asymptotics of the complete cosecant sum. Targeted searches for coprime/reduced-residue cosecant asymptotics did not locate a source stating exactly (17)--(20), but that absence is not treated as evidence of novelty. Formula (17) is an elementary Möbius consequence of the classical full-shell asymptotic (11), and (19) identifies its arithmetic content with a finite Euler product immediately.

Accordingly, the durable contribution here is the **prime-circle phase-boundary classification** completing the open `alpha<=1/2` sector of PC-386, not a claim that the analytic identities themselves are new. The result is a negative novelty audit for this scalar branch: the only arithmetic surviving the critical transition classicalizes before any nontrivial-zeta-zero structure appears.

## Sources

- Iaroslav V. Blagouchine and Eric Moreau, *On a finite sum of cosecants appearing in various problems*, Journal of Mathematical Analysis and Applications 539(1), 128515 (2024), DOI: 10.1016/j.jmaa.2024.128515; arXiv:2312.16657: https://arxiv.org/abs/2312.16657 . Source for complete asymptotic expansions and bounds for the full cosecant sum used in (11).
- The line registry `research/prime_circle/SOURCES.md` supplies the standing Möbius/Ramanujan, cyclotomic, harmonic-root, and related prior-art anchors.

## Relation to earlier findings

PC-384--PC-385 classify full-root mesh/submesh inverse-power chord laws as universal analytic sampling phenomena. PC-386 shows that exact-order primitive restriction restores a coprimality sieve in the supercritical range `alpha>1/2` and explicitly leaves `alpha<=1/2` open. The present result closes that stated gap: the critical and subcritical primitive regimes do not produce a stronger arithmetic mechanism, and the scalar phase diagram is exhausted at this level.