# ANF-011 — negative out-of-band tails violate the universal conjugate-pair barrier

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BOUNDARY`. `ANF-010` showed that BGSST already supplies the favorable analytic sign for a Cohn--Elkies negative spectral tail, while a single scalar PSD Gram kernel cannot carry that tail. The obstruction is in fact stronger: for every Fourier--Laplace-admissible scalar pair kernel, any nontrivial negative spectral mass beyond the known band forces the kernel to tend to `-infinity` on the imaginary axis. But the two-point conjugate configuration from `ANF-005` forces every universal affine simple-real counting certificate to keep that same kernel uniformly bounded below there. Hence **no universal affine scalar pair certificate can exploit a nontrivial Cohn--Elkies negative tail outside `[-1,1]`, even if PSD/Gram positivity is abandoned.**

## 1. Universal affine counting already imposes an imaginary-axis floor

Use the setup of `ANF-005`. Let `F : C -> C` be even and of real type and suppose that, for every nonempty finite multiset `Z` invariant under complex conjugation,

\[
s(Z)\ge A|Z|-\sum_{z,w\in Z}F(z-w),
\tag{1}
\]

where `s(Z)` counts simple real elements. Put

\[
d:=F(0),\qquad \delta:=1+d-A.
\tag{2}
\]

Applying (1) to one nonreal conjugate pair gives the exact necessary condition already derived in `ANF-005`:

\[
\boxed{F(iy)\ge 1-\delta\qquad(y\in\mathbb R,\ y\ne0).}
\tag{3}
\]

The point of the present finding is that the Cohn--Elkies tail sign from `ANF-010` is incompatible with (3) before any PSD or Hilbert-space structure is imposed.

## 2. A negative outer spectral tail dominates the Fourier--Laplace transform

Let `g : R -> R` be real and even, and suppose it is **Fourier--Laplace admissible** in the following explicit sense:

\[
\int_{\mathbb R}|g(\alpha)|e^{2\pi y|\alpha|}\,d\alpha<\infty
\qquad\text{for every }y>0.
\tag{4}
\]

Then

\[
F(z):=\widehat g(z)
=\int_{\mathbb R}g(\alpha)e^{-2\pi i\alpha z}\,d\alpha
\tag{5}
\]

is entire, and on the imaginary axis

\[
F(iy)=2\int_0^\infty g(\alpha)\cosh(2\pi\alpha y)\,d\alpha.
\tag{6}
\]

Assume the favorable tail sign used in the Cohn--Elkies/BGSST tail-drop:

\[
g(\alpha)\le0\qquad(|\alpha|>1).
\tag{7}
\]

If this tail is nontrivial, then `g<0` on a set of positive measure outside the unit band. Hence there exist `1<a<b` such that

\[
m:=-\int_a^b g(\alpha)\,d\alpha>0.
\tag{8}
\]

Let

\[
P:=\int_0^1 g_+(\alpha)\,d\alpha<\infty.
\tag{9}
\]

Because the rest of the tail is also nonpositive, (6)--(9) give, for `y>0`,

\[
\begin{aligned}
F(iy)
&\le 2P\cosh(2\pi y)
   +2\int_a^b g(\alpha)\cosh(2\pi\alpha y)\,d\alpha\\
&\le 2P\cosh(2\pi y)-2m\cosh(2\pi a y).
\end{aligned}
\tag{10}
\]

Since `a>1`, the second exponential grows strictly faster. Therefore

\[
\boxed{F(iy)\longrightarrow-\infty\qquad(y\to+\infty).}
\tag{11}
\]

This is only a Laplace-tail comparison: positive spectral mass is confined to the unit band, while any negative mass farther out receives a strictly larger exponential weight on the imaginary axis.

## 3. Universal affine Cohn--Elkies tails therefore collapse back to support one

Combine (3) and (11). If `delta` is finite, a universal affine counting inequality of the form (1) requires a fixed lower bound for `F(iy)` for every imaginary separation. A nontrivial negative spectral tail satisfying (7) makes that impossible.

Thus, within the Fourier--Laplace-admissible class,

\[
\boxed{
\text{(universal affine counting)}
+\text{(Cohn--Elkies tail sign)}
\Longrightarrow
 g(\alpha)=0\ \text{a.e. for }|\alpha|>1.
}
\tag{12}
\]

The conclusion does **not** use positive definiteness, a Gram representation, Bochner's theorem, or semidefinite duality. It therefore strengthens the scalar obstruction in `ANF-010`: replacing one PSD kernel by an indefinite scalar kernel, a signed scalar difference of PSD kernels, or any other scalar decomposition does not help if the final deterministic theorem is still a universal affine pair inequality with kernel `F=widehat g`.

The surviving global affine problem is exactly the support-one signed problem from `ANF-005`. Inside the band, `g` may still change sign and the unresolved objective remains whether the necessary finite-configuration constraints force

\[
M(F)+\delta\ge m_{\rm MT}.
\tag{13}
\]

What has been closed here is the apparently larger escape route of paying for an improvement using BGSST's unconditional positivity at `|alpha|>1` through a negative scalar spectral tail.

## 4. Relation to BGSST and the RH-conditional Cohn--Elkies method

BGSST prove unconditionally that their form factor is nonnegative for every real frequency. As `ANF-010` records, this means that a test profile with `g(alpha)<=0` outside the asymptotic band can discard the unknown out-of-band contribution on the **analytic** side. Chirre--Goncalves--de Laat exploit precisely this Cohn--Elkies sign pattern under RH, where zero differences are real and their zero-side kernel can be controlled by real-axis positivity.

Without RH, the zero differences are complex. Equation (12) explains a sharper reason why the same scalar tail cannot be combined with a Lamzouri-style universal complex-configuration count: the off-line conjugate-pair direction probes `widehat g` on the imaginary axis, where the negative outer tail is exponentially amplified rather than harmlessly discarded.

So the two sides ask the same tail to do opposite things:

\[
\text{BGSST frequency side: negative tail is favorable,}
\qquad
\text{complex-zero side: negative tail destroys the conjugate-pair floor.}
\tag{14}
\]

This localizes the remaining out-of-band frontier more tightly than `ANF-010`. Any successful use of BGSST positivity beyond support one must avoid the universal affine scalar-pair template itself, not merely avoid scalar PSD Gram kernels.

## 5. What remains genuinely open

The theorem does not rule out a counting inequality that is **not universal over arbitrary conjugation-invariant finite multisets**. Actual zeta zeros have global density, functional-equation symmetry, height structure and explicit-formula constraints that an isolated two-point configuration does not encode. A zeta-specific deterministic inequality could in principle use such structure.

It also does not rule out genuinely non-affine or pre-compression architectures: matrix order or inertia used before scalarization, local ordered configurations as in `ANF-006`, higher-order correlation information, or another functional that cannot be reduced to one affine scalar pair energy. Those routes evade the exact hypothesis (1), rather than evading the proof of (12).

Condition (4) is also substantive. It guarantees that the same Fourier profile used on the BGSST side defines the complex zero-side kernel by the Fourier--Laplace integral at arbitrary imaginary separations. Compactly supported profiles satisfy it automatically, as do the standard Gaussian-polynomial test functions used in many SDP constructions. If a proposed profile has no such complex evaluation, then this theorem does not apply to it -- but neither can it be inserted into (1) through the representation (5) without an additional analytic continuation argument that must itself be justified.

## 6. Prior-art and novelty assessment

The source ingredients are established. BGSST supply the unconditional all-frequency nonnegativity of the form factor and its Fourier bridge; Chirre--Goncalves--de Laat supply the RH-conditional Cohn--Elkies sign architecture; Lamzouri supplies the successful universal Hilbert-space complex-zero count; and `ANF-005` already extracted the conjugate-pair lower barrier (3). The dominance estimate (10) is an elementary Fourier--Laplace observation.

A targeted search of the pair-correlation/Cohn--Elkies literature and current exploratory work around transplanting the SDP class did not locate a source formulating this exact universal-affine imaginary-axis obstruction. No publication-level novelty claim is made. The durable Mathia contribution is the structural reduction (12): **once arbitrary complex conjugate configurations must be counted by one affine scalar pair energy, every useful negative out-of-band Cohn--Elkies tail is impossible regardless of PSD structure.**

## 7. Decisive audit boundary

The result can fail only by leaving one of its explicit hypotheses. A counterexample would need either a nontrivial `g<=0` outside `[-1,1]` satisfying (4) whose transform does not tend to `-infinity` on the imaginary axis, contradicting (10), or a universal affine certificate (1) that violates the conjugate-pair test (3), contradicting direct evaluation on `Z={iy,-iy}`.

For future work the routing is therefore exact. Do not spend effort widening a universal scalar affine profile beyond support one merely because BGSST is positive there. Either solve the still-open signed support-one extremal problem of `ANF-005`, or change the zero-side information carrier so that the isolated conjugate-pair obstruction is no longer the governing universal test.