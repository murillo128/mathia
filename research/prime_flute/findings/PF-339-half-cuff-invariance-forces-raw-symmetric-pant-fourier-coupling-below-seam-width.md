# PF-339 — half-cuff invariance forces raw symmetric-pant Fourier coupling below the seam-width scale

**Status:** `EXACT-DERIVED + RAW-FOURIER-THRESHOLD + TWO-MODE-PDE-REDUCTION + ROUTE-SHARPENING`.

PF-338 reduces the live PF-336 translation route, on the arithmetic subsequence `r_n=h_{n+1}/h_n\to0`, to asymptotic half-cuff invariance of the normalized pant insertion

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2}.
\]

PF-326 makes the remaining seam normalization explicit on every fixed physical band. Combining the two gives a substantially cheaper obstruction test: in the **symmetric seam face-parity channel**, every fixed odd Fourier coupling of the raw pant DtN compression must be smaller than the seam width itself.

More precisely, let `w_n` be the PF-205 seam half-width and let

\[
e_{n,k}(s)=\ell_n^{-1/2}e^{2\pi i k s/\ell_n},
\qquad k\ne0,
\]

with fixed nonzero indices `j,k` satisfying `j-k` odd. For all large `n` these modes lie in every fixed nonconstant physical-low band. If `\Lambda^{(+)}_{n;jk}` denotes the corresponding matrix entry of the symmetric-face-parity compression of `\Lambda_{LL,n}`, then the PF-336 translation gate implies

\[
\boxed{\Lambda^{(+)}_{n;jk}=o(w_n).}
\]

Since PF-205 gives `w_n\asymp P_n^{-1}`, this is equivalently

\[
\boxed{\Lambda^{(+)}_{n;jk}=o(P_n^{-1}).}
\]

Thus the normalized half-cuff test does **not** require computing a large matrix. It is already falsified by one fixed pair of nonconstant Fourier modes if their raw symmetric-pant coupling is merely of seam-width size or larger. In particular the fixed pair `k=1`, `j=2` is enough.

There is a basis-free two-mode version. Put

\[
c_{n,m}(s)=\sqrt{\frac2{\ell_n}}\cos\frac{2\pi m s}{\ell_n},
\qquad m=1,2,
\]

and

\[
f_{n,+}=\frac{c_{n,2}+c_{n,1}}{\sqrt2},
\qquad
f_{n,-}=\frac{c_{n,2}-c_{n,1}}{\sqrt2}.
\]

The half-cuff translation `H_n=\tau_{\ell_n/2}` satisfies

\[
H_nf_{n,+}=f_{n,-},
\]

and PF-338 plus PF-326 force, in the symmetric face-parity channel,

\[
\boxed{
\left|
\langle f_{n,+},\Lambda^{(+)}_{LL,n}f_{n,+}\rangle
-
\langle f_{n,-},\Lambda^{(+)}_{LL,n}f_{n,-}\rangle
\right|
=o(w_n)=o(P_n^{-1}).
}
\]

This is now the cheapest concrete PDE falsifier on the finite-boundary subsequence: compare the raw one-cusp-pant energies of two explicit nonconstant low-frequency boundary data related by half-cuff translation. Any lower limsup after division by `w_n`, even a finite nonzero one, kills the PF-336 translation route.

## Claim

Fix one retained physical-low cuff component and the symmetric (`+`) seam face-parity channel. Let `Q_{n,+}` be the corresponding PF-205 seam form and let

\[
\Lambda^{(+)}_n
\]

be the same-channel compression of the raw low-side pant DtN insertion. In the physical Fourier basis write

\[
q_{n,+}(k)
:=\langle e_{n,k},Q_{n,+}e_{n,k}\rangle,
\qquad
\lambda^{(+)}_{n;jk}
:=\langle e_{n,j},\Lambda^{(+)}_ne_{n,k}\rangle.
\]

For every fixed nonzero integer `k`, PF-326 gives

\[
\boxed{
q_{n,+}(k)
=w_n\left(1+O(w_n^2+\ell_n^{-2})\right).
}
\tag{1}
\]

Consequently, for fixed nonzero `j,k`,

\[
\boxed{
(K_n)_{jk}
=\frac{\lambda^{(+)}_{n;jk}}{w_n}
\left(1+O(w_n^2+\ell_n^{-2})\right).
}
\tag{2}
\]

Along the PF-324 subsequence `r_n\to0`, if the PF-336 translation gate

\[
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\tag{3}
\]

holds, PF-338 implies

\[
\sum_{a-b\ \mathrm{odd}}|(K_n)_{ab}|^2=o(1).
\tag{4}
\]

Therefore every fixed retained odd-offset entry satisfies `(K_n)_{jk}=o(1)`, and (2) yields

\[
\boxed{
\lambda^{(+)}_{n;jk}=o(w_n)
\qquad (j-k\ \mathrm{odd}).
}
\tag{5}
\]

PF-205/PF-107 give `w_n\asymp P_n^{-1}`, so (5) is equivalent to `o(P_n^{-1})`.

For comparison, the antisymmetric seam parity has

\[
q_{n,-}(k)
=w_n^{-1}\left(1+O(w_n^2+\ell_n^{-2})\right),
\tag{6}
\]

so the same normalized necessary condition yields only

\[
\lambda^{(-)}_{n;jk}=o(w_n^{-1}).
\tag{7}
\]

The symmetric channel is therefore the sharp raw-DtN falsifier: its seam normalization magnifies fixed low-frequency raw coupling by `w_n^{-1}\asymp P_n`.

## 1. Fixed Fourier indices stay inside the retained nonconstant low band

PF-318's direct target is the retained **nonconstant** physical-low space. The zero mode is therefore unnecessary here. For any fixed `m\ne0`,

\[
\xi_{n,m}=\frac{2\pi m}{\ell_n}\longrightarrow0
\]

because `\ell_n\to\infty`. Hence every fixed pair such as `m=1,2` belongs to the retained nonconstant low band for all sufficiently large `n`, independently of the exact positive physical cutoff.

PF-326 gives, for the flat strip model,

\[
q_+(\xi,w)=\mu\tanh(\mu w),
\qquad
\mu=\sqrt{1+\xi^2},
\]

and proves that the actual hyperbolic seam has the same fixed-band asymptotics up to relative `1+O(w_n^2)`. For fixed `m`, `\mu=1+O(\ell_n^{-2})`; Taylor expansion therefore gives (1). The same argument with `q_-(\xi,w)=\mu\coth(\mu w)` gives (6).

No condition number or operator norm of `K_n` enters this reduction. On fixed modes the normalizer is just an explicit scalar asymptotic.

## 2. PF-338 converts normalized half-cuff invariance into raw `o(w_n)` coupling

Because `Q_{n,+}` is Fourier diagonal, the matrix of the normalized insertion is exactly

\[
(K_n)_{jk}
=\frac{\lambda^{(+)}_{n;jk}}
{\sqrt{q_{n,+}(j)q_{n,+}(k)}}.
\tag{8}
\]

Equation (1) turns the denominator into

\[
\sqrt{q_{n,+}(j)q_{n,+}(k)}
=w_n\left(1+O(w_n^2+\ell_n^{-2})\right)
\]

for every fixed pair, proving (2).

PF-338 is stronger than a fixed-diagonal statement: on `r_n\to0` the complete retained odd-offset Hilbert--Schmidt mass must vanish if (3) is true. Since every summand is nonnegative, each fixed odd-offset matrix entry tends to zero individually. Combining with (2) proves (5).

This changes the scale of the live PDE question. Showing merely

\[
|\lambda^{(+)}_{n;2,1}|\gtrsim w_n
\]

along any further subsequence is already enough to refute the translation route. An order-one raw coupling would exceed the required threshold by a factor comparable to `P_n`.

## 3. A two-mode variational witness removes Fourier-matrix bookkeeping

The real modes `c_{n,1}` and `c_{n,2}` are orthonormal and lie in opposite half-cuff parity sectors:

\[
H_nc_{n,1}=-c_{n,1},
\qquad
H_nc_{n,2}=c_{n,2}.
\]

Therefore `f_{n,+}` and `f_{n,-}` are unit vectors and are exchanged by `H_n`. Let

\[
\mathcal E_n^{(+)}(f)
:=\langle f,\Lambda^{(+)}_nf\rangle.
\]

Polarization gives

\[
\mathcal E_n^{(+)}(f_{n,+})
-
\mathcal E_n^{(+)}(f_{n,-})
=2\operatorname{Re}
\langle c_{n,2},\Lambda^{(+)}_nc_{n,1}\rangle.
\tag{9}
\]

Every complex Fourier entry contributing to the right-hand side has odd index difference. Equation (5), or equivalently PF-338 applied on this fixed two-dimensional sector together with (1), therefore gives

\[
\boxed{
\mathcal E_n^{(+)}(f_{n,+})
-
\mathcal E_n^{(+)}(f_{n,-})
=o(w_n).
}
\tag{10}
\]

Thus one does not need a full DtN matrix or an aggregate Hilbert--Schmidt calculation to falsify the route. A direct variational comparison of these two explicit boundary data suffices.

The pair also lines up with PF-215's exact tight-pant corridor coordinate. Taking `s=0` at the finite-cuff common-perpendicular foot,

\[
f_{n,+}(0)=\frac{2}{\sqrt{\ell_n}},
\qquad
f_{n,-}(0)=0,
\]

and `f_{n,-}` has a quadratic zero there, while `f_{n,+}` does not. Half-cuff translation exchanges the two profiles. This makes the pair a natural probe of the geometric asymmetry between the short finite-cuff corridor and its antipodal boundary region.

That observation is **not** yet an energy lower bound. PF-215 controls the short corridor but does not supply the complementary global upper estimate needed to prove that the total pant energies of the two profiles differ by `\gtrsim w_n`. The missing calculation is now explicit rather than hidden inside the normalized operator.

## 4. Prior-art and novelty audit

No novelty is claimed for Fourier diagonalization of the seam strip, quadratic-form polarization, or the fact that Hilbert--Schmidt convergence forces each fixed matrix entry to vanish. PF-326 already audits the finite-strip `tanh/coth` DtN formulas used in (1) and (6).

A targeted check of the Steklov/Dirichlet-to-Neumann literature found general spectral and pseudodifferential descriptions of DtN operators, including the standard first-order boundary symbol and broad hyperbolic/inverse-boundary results, but no result that supplies the project-specific `o(w_n)` fixed-mode coupling required for this degenerating one-cusp-pant family. No new external theorem is used here, so `SOURCES.md` needs no additional dependency.

The Mathia-specific content is the scale conversion: PF-338's half-cuff Hilbert--Schmidt obstruction plus PF-326's exact seam normalization turns a normalized operator condition into the raw scalar threshold (5), and then into the explicit two-mode energy test (10).

## 5. Boundaries and falsification

1. **Necessary condition only.** Equations (5) and (10) follow if the PF-336 translation gate holds; they do not prove that the actual pant violates it.
2. **Arithmetic subsequence.** The use of PF-338 is on the PF-324 source-realized subsequence `r_n\to0`. No whole-tail half-cuff conclusion is asserted.
3. **Nonconstant modes only.** The reduction deliberately uses fixed modes `1` and `2` in Fourier index, not the excluded constant mode of PF-318's retained direct target.
4. **Symmetric seam parity is the strong test.** The antisymmetric normalization gives only (7); this finding does not claim an obstruction there.
5. **PF-215 is motivation, not completion.** The common-perpendicular corridor explains why the explicit pair in (9) is geometrically discriminating, but a rigorous comparison of the *total* one-cusp-pant energies is still required.
6. **No principal-symbol shortcut.** Fixed Fourier indices have physical frequencies tending to zero, so standard high-frequency DtN principal-symbol asymptotics do not decide (5).
7. **No completed-angle conclusion yet.** Until a raw energy contrast larger than `o(w_n)` is proved, PF-336's translation route remains open. No scattering, zeta-zero, critical-line, or RH consequence follows.

A falsification of this finding would have to break PF-338's odd-sector implication, PF-326's fixed-band seam asymptotics, or the exact matrix identity (8). The unresolved mathematical question is instead whether the actual one-cusp-pant DtN response satisfies the extraordinarily small raw coupling required by (5).

## Consequence for the research line

The next obstruction-side PDE calculation should start with the symmetric seam parity and the explicit pair `f_{n,+},f_{n,-}` above. The target is no longer a qualitative statement that the pant is not half-cuff symmetric. It is the quantitative scalar test

\[
\boxed{
\frac{
|\mathcal E_n^{(+)}(f_{n,+})-\mathcal E_n^{(+)}(f_{n,-})|
}{w_n}
\not\longrightarrow0.
}
\]

Any such result closes the PF-336 translation branch negatively on the `r_n\to0` subsequence. Only if this two-mode contrast is `o(w_n)` should effort return to higher odd modes, the surviving even-offset/fixed-physical-separation sector, or a positive full-commutator estimate.