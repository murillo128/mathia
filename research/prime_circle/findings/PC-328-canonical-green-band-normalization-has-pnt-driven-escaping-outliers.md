# PC-328 — canonical Green band normalization has PNT-driven escaping outliers

**Status:** `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` + `MATCHED-CONTROL-OBSTRUCTION` for the canonical-source growing-conductor Green escape left open by PC-327.

PC-327 proves that, for arbitrary nonzero centered periodic masks, normalizing the cross-level Green operator by its intrinsic Hilbert-band scale makes the trace-class defect leave every uniformly bounded `S_2` and `S_1` family as the conductors grow. That result is deliberately source-independent and therefore does not decide whether the **canonical prime-support source** might nevertheless have a useful bounded spectral core after one subtracts the universal generalized-Hilbert singularity.

For the canonical source there is a stronger obstruction. A single fixed Fourier mode already has a classical prime-number-theorem asymptotic of size `1/log q`. The intrinsic Hilbert-band scale is only `sqrt(log q/q)`. Consequently the full band-normalized Green operator has discrete eigenvalue pairs escaping to infinity at least as

\[
\boxed{
\frac{\sqrt{qr}}
{(\log q\,\log r)^{3/2}}
}
\]

for two growing prime conductors `q,r`. This also forces the **operator norm** of the band-normalized trace-class defect to diverge, much more strongly than the universal Schatten lower bound of PC-327. The escaping pair is not a zero-sensitive effect: its leading fixed-mode amplitude is supplied by the smooth `Li`/PNT source profile, and PC-325 gives exact non-arithmetic phase controls with the same complete Green spectrum.

Thus the raw canonical Green family has no bounded band-normalized spectral limit. Any surviving growing-conductor program must first deflate or otherwise renormalize the fixed low-frequency PNT/Li source modes, in addition to controlling the universal generalized-Hilbert offset singularity isolated by PC-327.

## 1. Canonical source and its first nonzero Fourier mode

Let `q>3` be prime and retain the canonical prime-support source used in PC-311 onward,

\[
P_q:=\{p:2<p<q,\ p\text{ prime}\},
\qquad
R_q:=|P_q|=\pi(q)-2,
\tag{1}
\]

and

\[
f_q(x)=\frac{1}{R_q}\mathbf 1_{P_q}(x)-\frac1q,
\qquad x\in\mathbb Z/q\mathbb Z.
\tag{2}
\]

With the Fourier convention already used in PC-311--PC-327, its nonzero modes are

\[
a_q(h)
=\widehat f_q(h)
=\frac1{R_q}
\sum_{p\in P_q}e^{-2\pi i hp/q},
\qquad h\not\equiv0\pmod q.
\tag{3}
\]

Fix an integer `h>=1` while `q->infinity` through primes, and write `L=log q`. The quantitative prime number theorem used in PC-277, followed by Stieltjes partial summation for the smooth weight

\[
F_h(t)=e^{-2\pi iht},
\tag{4}
\]

gives

\[
\sum_{p\in P_q}F_h(p/q)
=
\int_2^q\frac{F_h(x/q)}{\log x}\,dx
+O_h\!\left(qe^{-c\sqrt L}\right).
\tag{5}
\]

The omission of the endpoints contributes only `O(1)`. After `x=qt`, split the integral at `t=q^{-1/2}`. The lower interval is exponentially negligible on the `q/L^3` scale, while on the upper interval

\[
\frac1{L+\log t}
=
\frac1L-\frac{\log t}{L^2}
+O\!\left(\frac{(\log t)^2}{L^3}\right).
\tag{6}
\]

Because `h` is a nonzero integer,

\[
\int_0^1F_h(t)\,dt=0.
\tag{7}
\]

Hence, with

\[
\boxed{
C_h:=-\int_0^1 e^{-2\pi iht}\log t\,dt,
}
\tag{8}
\]

we obtain

\[
\int_2^q\frac{F_h(x/q)}{\log x}\,dx
=
\frac{qC_h}{L^2}
+O_h\!\left(\frac q{L^3}\right).
\tag{9}
\]

Also

\[
R_q
=\frac qL\left(1+\frac1L+O(L^{-2})\right),
\tag{10}
\]

so (3), (5), and (9) give the fixed-mode asymptotic

\[
\boxed{
a_q(h)=\frac{C_h}{\log q}
+O_h\!\left(\frac1{(\log q)^2}\right).}
\tag{11}
\]

The constant is already nonzero at `h=1`. In fact

\[
\operatorname{Re}C_1
=\frac{\operatorname{Si}(2\pi)}{2\pi}>0,
\tag{12}
\]

so `C_1!=0`. More explicitly,

\[
C_1
=
\frac{\operatorname{Si}(2\pi)}{2\pi}
+i\,\frac{\operatorname{Ci}(2\pi)-\gamma-\log(2\pi)}{2\pi}.
\tag{13}
\]

Nothing zero-sensitive entered this derivation. Equation (11) is the first smooth logarithmic-density correction left after the uniform Fourier coefficient cancels.

## 2. The intrinsic Hilbert-band scale is much smaller

Parseval for the centered source (2) gives the exact RMS identity already implicit in PC-323/PC-327,

\[
\boxed{
\mu_q
:=\frac1q\sum_{j=1}^{q-1}|a_q(j)|^2
=\frac1{R_q}-\frac1q.}
\tag{14}
\]

Using (10),

\[
\boxed{
\mu_q
\sim\frac{\log q}{q}.}
\tag{15}
\]

For two distinct prime conductors `q,r`, PC-323 identifies the unique absolutely-continuous Hilbert-band scale as

\[
\boxed{
c_{q,r}=\sqrt{\mu_q\mu_r}
\sim
\sqrt{\frac{\log q\,\log r}{qr}}.}
\tag{16}
\]

Thus a fixed canonical Fourier coefficient decays only logarithmically, while the spectral band carrying the residue-averaged Hilbert channel collapses at an essentially square-root conductor scale.

## 3. One matrix coefficient forces escaping discrete spectrum

The canonical downstream Green operator of PC-322--PC-323 is

\[
X_{q,r}(k,l)
=\frac{a_q(k)a_r(l)}{k+l},
\qquad k,l\ge1,
\tag{17}
\]

with self-adjoint dilation

\[
G_{q,r}
=
\begin{pmatrix}
0&X_{q,r}\\
X_{q,r}^*&0
\end{pmatrix}.
\tag{18}
\]

The single `(1,1)` matrix coefficient gives the exact elementary lower bound

\[
\|X_{q,r}\|
\ge
\frac{|a_q(1)a_r(1)|}{2}.
\tag{19}
\]

Combining (11), (16), and (19),

\[
\boxed{
\frac{\|G_{q,r}\|}{c_{q,r}}
=
\frac{\|X_{q,r}\|}{c_{q,r}}
\ge
\frac{|C_1|^2}{2}
\frac{\sqrt{qr}}
{(\log q\,\log r)^{3/2}}
\bigl(1+o(1)\bigr).}
\tag{20}
\]

The right side tends to infinity whenever both conductors tend to infinity. In the comparable case `q asymp r asymp Q`, it grows at least as

\[
\boxed{
\frac{|C_1|^2}{2}\,
\frac{Q}{(\log Q)^3}
\bigl(1+o(1)\bigr).}
\tag{21}
\]

PC-323 gives, for every fixed pair `(q,r)`,

\[
\sigma_{\rm ess}(G_{q,r})
=[-\pi c_{q,r},\pi c_{q,r}].
\tag{22}
\]

Therefore the normalized operators

\[
\widetilde G_{q,r}:=G_{q,r}/c_{q,r}
\tag{23}
\]

all have the same essential band `[-pi,pi]`, while (20) forces their norms to infinity. Since `G_{q,r}` is self-adjoint and differs from its Hilbert core by a trace-class operator, every spectral point outside (22) is discrete. The off-diagonal dilation has symmetric spectrum. Hence for all sufficiently large `q,r` there is a discrete eigenvalue pair

\[
\boxed{
\pm\lambda_{q,r},
\qquad
\lambda_{q,r}
\ge
\frac{|C_1|^2}{2}
\frac{\sqrt{qr}}
{(\log q\,\log r)^{3/2}}
\bigl(1+o(1)\bigr).}
\tag{24}
\]

This is stronger than failure of a Schatten bound: spectral mass itself escapes arbitrarily far from the fixed Hilbert band.

## 4. The canonical trace-class defect diverges already in operator norm

Write the PC-323 decomposition

\[
G_{q,r}=G_{0;q,r}+V_{q,r},
\tag{25}
\]

where `G_0` is the rank-one finite channel tensored with the classical Hilbert matrix and `V` is the self-adjoint dilation of the trace-class defect `S`. The Hilbert core satisfies

\[
\|G_{0;q,r}\|=\pi c_{q,r}.
\tag{26}
\]

Therefore (20) and the triangle inequality give

\[
\boxed{
\frac{\|V_{q,r}\|}{c_{q,r}}
\ge
\frac{|C_1|^2}{2}
\frac{\sqrt{qr}}
{(\log q\,\log r)^{3/2}}
\bigl(1+o(1)\bigr)-\pi.}
\tag{27}
\]

Since `V` is the self-adjoint dilation of `S`, `||V||=||S||`. Thus the canonical defect is not merely non-uniform in trace or Hilbert-Schmidt norm: its **band-normalized operator norm diverges**. In particular,

\[
\frac{\|S_{q,r}\|_2^2}{c_{q,r}^2}
\ge
\left(
\frac{|C_1|^2}{2}
\frac{\sqrt{qr}}
{(\log q\,\log r)^{3/2}}
\bigl(1+o(1)\bigr)-\pi
\right)^2,
\tag{28}
\]

once the parenthesis is positive. For `q asymp r asymp Q`, this is at least of order `Q^2/(log Q)^6`, vastly stronger for the canonical source than PC-327's universal `Omega(log Q)` Hilbert-Schmidt floor.

PC-327 remains essential: its logarithmic lower bound applies to **every** nonzero centered source and identifies the source-independent generalized-Hilbert corner singularity. Equation (28) is a different phenomenon: the canonical prime-support source additionally carries slowly decaying low Fourier modes whose normalization against the shrinking RMS band creates much larger outliers.

## 5. Matched controls show that the outliers are not an RH signal

The leading input (11) is already classical PNT/Li data. PC-277 constructs a non-prime denominator-`q` Li-grid control whose normalized source measure matches the prime source throughout the quantitative PNT transport regime. For each fixed Fourier mode its coefficient therefore has the same `C_h/log q` leading behavior. Thus even the mechanism producing the lower bound (20) does not require explicit-formula oscillations or zeta zeros.

There is also an exact operator-level obstruction. PC-325 proves that conjugate-symmetric phase twists of the periodic Fourier masks preserve `|a(k)|`, `|b(l)|` and simultaneously conjugate the complete Green operator. Hence there are non-arithmetic periodic controls with **exactly the same Green spectrum**, including the escaping outlier pair (24). The outlier is therefore a genuine spectral feature of the canonical normalization but not a prime-specific discriminator.

This distinction matters. The result does not say that all source-sensitive information in the growing-conductor Green family is classical. It says that the first and largest obstruction to a bounded raw spectral limit is already generated by smooth low-frequency prime-density data and is exactly reproducible by matched controls.

## 6. Prior-art and novelty audit

No ingredient of the derivation is individually new. The weighted fixed-mode asymptotic (11) is standard quantitative PNT plus partial summation; PC-277 already anchors the required de la Vallée-Poussin-scale estimate through Montgomery--Vaughan. The Hilbert spectrum and generalized-Hilbert channel are classical Magnus/Rosenblum territory and were already audited in PC-323. The estimate `||X||>=|X_{11}|` and the compact-perturbation conclusion outside the essential band are elementary operator theory.

A targeted audit of weighted sums of smooth functions over primes and generalized Hilbert matrices found the expected classical literatures, including standard weighted-prime asymptotics and the established spectral theory of shifted Hilbert matrices. It did not reveal an existing theorem asserting this specific Prime-Circle synthesis: the canonical centered prime-support Fourier mask, normalized by its own RMS Hilbert band, forces a discrete Green outlier pair of size at least (24). Accordingly this finding claims **project-local boundary content**, not a new prime-number-theorem or Hilbert-operator theorem.

The novelty check also cuts against a positive RH interpretation. Equation (24) is explained without an explicit formula, and PC-325 supplies exact isospectral non-arithmetic controls. The correct use of the result is therefore as a normalization/deflation obstruction.

## 7. Boundary and next decisive test

The result closes the raw route

\[
\text{canonical prime-support Green operator}
\to
\text{normalize only by the Hilbert band}
\to
\text{bounded growing-conductor spectral limit}.
\tag{29}
\]

A surviving Green program must remove more than the universal generalized-Hilbert offset singularity of PC-327. It must also neutralize the source-forced fixed low modes whose `1/log q` PNT amplitudes dominate the `sqrt(log q/q)` band scale.

The natural next test is therefore **low-mode deflation with a matched smooth reference**: subtract the finite fixed-mode packet predicted by the Li/PNT expansion, then ask whether the residual band-normalized operator is tight and whether any remaining spectral statistic separates the canonical source from the PC-325/PC-277 controls. PC-275--PC-281 warn that every fixed or sufficiently regular low-frequency packet is Li-reproducible, so a positive result must identify a residual mechanism that survives that control rather than merely move the same smooth bias into another spectral coordinate.

This finding does **not** prove that finitely many low modes suffice to renormalize the whole family, does not identify the asymptotic top eigenvalue, and does not exclude a zero-sensitive residual after a source-derived deflation. Those are separate questions.

## 8. Falsification hooks

This finding should be revised or withdrawn if any of the following occurs:

1. the canonical Fourier convention in PC-311--PC-327 is shown not to give (3) for nonzero modes;
2. the fixed-mode PNT asymptotic (11) fails under the exact canonical source normalization;
3. the Parseval scale (14) or the Hilbert-band normalization (16) differs from the operator normalization actually used in PC-323;
4. the Green kernel is shown not to contain the `(1,1)` entry in (17), invalidating the operator-norm lower bound;
5. prior art is found that already states this exact canonical-source/band-normalized escaping-outlier mechanism, in which case the novelty classification should be downgraded to pure classicalization.

Absent such a failure, the durable conclusion is narrow but decisive: **before any RH-sensitive growing-conductor Green limit can be interpreted, the canonical low-frequency PNT/Li outliers must be removed or explicitly incorporated into the reference operator.**