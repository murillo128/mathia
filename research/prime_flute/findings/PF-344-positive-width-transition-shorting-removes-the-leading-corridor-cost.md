# PF-344 — a positive-width transition band shorts out the leading corridor cost

**Status:** EXACT-DERIVED + VARIATIONAL-SCHUR-SHORTING + EXPONENTIAL-EDGE-CANCELLATION + WEIGHTED-EXPONENTIAL-COMPLETENESS + ENDPOINT-OPEN.

PF-343 proves a noncompact **direct** hard-sector angle when two bounded physical Fourier modes lie in opposite sectors and are sufficiently close. It explicitly leaves open the different architecture in which a physical transition band is retained in the full positive boundary precision and eliminated by a Schur complement.

That architecture does suppress the very corridor-scale term that drives PF-342/PF-343. There are two distinct statements:

1. For low/high modes immediately adjacent to the two edges of a fixed positive-width transition band, binomial transition-mode compensators improve the shorted diagonal-energy and mixed-entry upper bounds from \(O(1+D_n/L_n^2)\) to \(O(D_n e^{-\gamma L_n})\) for some \(\gamma>0\); this is **relative to the raw corridor scale**, not an absolute-energy or normalized-angle bound.
2. More generally, **every individual bounded-physical-frequency cosine mode** has shorted energy \(o(D_n)\) when the full growing transition band is available. The second statement uses classical weighted exponential completeness and is qualitative; its approximation coefficients need not have a uniform norm or any useful rate.

Here \(D_n=L_n^{-1}(s_{n-1}^{-1}+s_n^{-1})\to\infty\) is PF-343's symmetric two-pant corridor scale. These facts show that the leading direct-angle witness is **not stable under exact positive shorting**. They do **not** prove the effective, *diagonally normalized* low/high angle is compact or weak trace class: the shorted diagonal energies decrease along with the mixed term.

## Claim

Fix physical cutoffs \(0<\kappa_-<\kappa_+<\infty\) independent of the tail index. In every sufficiently large canonical finite section, partition the boundary Fourier variables modulewise into low, transition, and high sectors

\[
\mathcal B=\mathcal L\oplus\mathcal T\oplus\mathcal H,\quad
\mathcal T_n=
\operatorname{span}\{e^{i\xi t}:\kappa_-<|\xi|<\kappa_+,\ \xi=2\pi k/L_n\}.
\tag{1}
\]

Let \(M=Q+\Lambda_E>0\) be the **complete raw positive simultaneous-seam precision** of PF-214/PF-317, restricted to that finite section. Write \(X=\mathcal L\oplus\mathcal H\) and form the exact positive shorted form

\[
S=M^{/\mathcal T}
=M_{XX}-M_{X\mathcal T}M_{\mathcal T\mathcal T}^{-1}M_{\mathcal T X}.
\tag{2}
\]

The inverse is the finite-section positive inverse; no infinite-section inverse is asserted. For every \(x\in X\),

\[
\boxed{\langle x,Sx\rangle
=\min_{t\in\mathcal T}\langle x+t,M(x+t)\rangle.}
\tag{3}
\]

Let \(L_n\) be the physical cuff period and \(s_{n-1},s_n\) the two adjacent PF-341 finite--finite core separations. Put

\[
D_n=\frac1{L_n}\left(\frac1{s_{n-1}}+\frac1{s_n}\right)\longrightarrow\infty.
\tag{4}
\]

Use the normalized cosine vectors in the symmetric two-face seam-parity channel, with physical origin at the common-perpendicular foot. Let \(\ell_n\) be the last nonconstant low mode below \(\kappa_-\), \(h_n\) the first high mode at or above \(\kappa_+\), and let \(t_n^-\) and \(t_n^+\) be the immediately neighboring transition modes at the lower and upper edges. The latter exist for all sufficiently large \(n\), because the width \(\kappa_+-\kappa_->0\) is fixed and \(L_n\to\infty\).

Uniformly over all canonical finite sections containing these modes,

\[
\boxed{
0\le
\langle \ell_n,S\ell_n\rangle,\;
\langle h_n,Sh_n\rangle
\le C\left(1+\frac{D_n}{L_n^2}+w_n\right)
}
\tag{5}
\]

and, by positivity,

\[
\boxed{
|\langle h_n,S\ell_n\rangle|
\le C\left(1+\frac{D_n}{L_n^2}+w_n\right)
=o(D_n).
}
\tag{6}
\]

Here \(w_n\to0\) is the PF-205 seam half-width. In particular

\[
\boxed{
\frac{\langle \ell_n,S\ell_n\rangle+
\langle h_n,Sh_n\rangle+
|\langle h_n,S\ell_n\rangle|}{D_n}
\longrightarrow0.
}
\tag{7}
\]

There is also a qualitative **whole bounded-band** statement. For any fixed \(K<\infty\) and any sequence of nonconstant Fourier cosine modes \(c_{n,\xi_n}\), with \(0<\xi_n\le K\), that lie outside \(\mathcal T_n\),

\[
\boxed{
\frac{\langle c_{n,\xi_n},S c_{n,\xi_n}\rangle}{D_n}
\longrightarrow0,
}
\tag{8}
\]

uniformly over the choice of such \(\xi_n\) and over containing canonical finite sections with the full physical transition sector. Consequently any pair of such modes obeys

\[
\boxed{
|\langle c_{n,\xi_n},S c_{n,\zeta_n}\rangle|
=o(D_n).
}
\tag{9}
\]

The uniformity in (8)--(9) concerns **individual normalized Fourier matrix entries relative to \(D_n\)**, not the norm of \(S\) on a growing-dimensional band and not the completed canonical-correlation angle.

If the transition width \(\eta=\kappa_+-\kappa_-\) is small enough that the edge pair \((\ell_n,h_n)\) satisfies PF-343's fixed physical-gap hypothesis, then its *raw* mixed form is at least \(cD_n\). Equations (2) and (6) therefore imply the explicit leading-scale cancellation

\[
\boxed{
\langle h_n,M_{X\mathcal T}M_{\mathcal T\mathcal T}^{-1}
M_{\mathcal T X}\ell_n\rangle
=
\langle h_n,M\ell_n\rangle+o(D_n).
}
\tag{10}
\]

This is a cancellation in an unnormalized **matrix element**; it is not a trace-ideal theorem. Section 4 strengthens the edge bounds (5)--(7) to an exponential decay rate relative to \(D_n\). The globally bounded-frequency statement (8)--(9) remains qualitative.

## 1. A reusable upper trial from the canonical one-cusp pant

Let \(A(s,L)\) be the positive shifted self-DtN form of one PF-341/PF-342 one-cusp pant, viewed from one finite boundary of period \(L\), with zero datum on the other finite boundary. Work in the canonical regime \(L\to\infty\), \(sL\to0\), and fix a bounded physical frequency window \([0,K]\).

For any finite trigonometric datum

\[
f_L(t)=\sqrt{\frac2L}
\sum_{j=1}^m a_j\cos(\xi_jt),
\quad
0\le\xi_j\le K,
\qquad
A_f=\sum_j|a_j|,
\tag{11}
\]

the raywise linear extension from PF-341, followed by its noncollapsing/cusp-side chart extension, gives

\[
\boxed{
\mathcal E_{A(s,L)}(f_L)
\le
\frac{C_K}{sL}
\int_{\mathbb R}
\left|\sum_{j=1}^m a_j\cos(\xi_jt)\right|^2
\operatorname{sech}t\,dt
+
C_K A_f^2.
}
\tag{12}
\]

Here and below the constants are independent of \(s,L,m\) provided \(K\) and \(A_f\) are specified.

To verify (12), PF-341's remaining core-ray length satisfies
\(c_0s\cosh t\le\ell(t)\le C_0s\cosh t\) on the growing collapsing corridor, with bounded logarithmic derivative. Its raywise trial bounds transverse energy by \(C(sL)^{-1}\int |\sum a_j\cos(\xi_jt)|^2\operatorname{sech}t\,dt\). Tangential and positive-shift energies there are \(O_K(A_f^2/L)\) because \(\sup(|f_L|+|f'_L|)\le C_KA_f/\sqrt L\) and \(\int s\cosh t\,dt=O(1)\). On the rest of the pant, the same \(O(L)\) unit-scale charts and cusp completion used in PF-341 cost \(O_K(A_f^2)\). Increasing the positive integrand from the finite corridor to \(\mathbb R\) proves (12). No claim about a new global DtN symbol is involved.

For the symmetric two-face cuff datum \(f_L\), PF-340 combines the two adjacent pant self-responses with fixed normalization factors. The seam form is Fourier diagonal and has the fixed-band eigenvalue \(q_+(\xi,w_n)=O_K(w_n)\). Thus the complete positive form on a datum supported on one cuff module obeys

\[
\boxed{
\mathcal E_M(f_L)
\le
C_KD_n
\int_{\mathbb R}
\left|\sum_j a_j\cos(\xi_jt)\right|^2
\operatorname{sech}t\,dt
+
C_K(1+w_n)A_f^2.
}
\tag{13}
\]

Zero twist ensures that the same physical cosine origin works on both adjacent pants. Formula (13) is a **trial upper bound**, not a two-sided equivalence.

## 2. One neighboring transition mode kills the edge \(D_n\) scale quantitatively

The Fourier spacing on cuff \(n\) is \(h_n=2\pi/L_n\). The lower-edge low and transition modes \(\ell_n,t_n^-\) differ in physical frequency by exactly \(h_n\); so do \(h_n,t_n^+\) at the upper edge.

Use (3) with transition compensators \(-t_n^-\) for \(\ell_n\) and \(-t_n^+\) for \(h_n\). The corresponding normalized boundary traces are **differences of two adjacent cosines** in the bounded physical band.

For any two frequencies \(\alpha,\beta\le K\), the mean-value theorem gives

\[
|\cos(\alpha t)-\cos(\beta t)|
\le|\alpha-\beta|\,|t|.
\tag{14}
\]

Since \(\int_{\mathbb R}t^2\operatorname{sech}t\,dt<\infty\), the weighted integral in (13) is \(O_K(h_n^2)=O_K(L_n^{-2})\), while the coefficient mass is \(A_f=2\). Hence

\[
\mathcal E_M(\ell_n-t_n^-),\;
\mathcal E_M(h_n-t_n^+)
\le C\left(1+\frac{D_n}{L_n^2}+w_n\right).
\tag{15}
\]

The variational characterization (3) immediately proves (5). Cauchy--Schwarz for the positive shorted form proves (6). Since \(D_n\to\infty\), \(L_n\to\infty\), and \(w_n\to0\), the ratio to \(D_n\) tends to zero. This proves (7).

Crucially, no conditioning estimate for \(M_{\mathcal T\mathcal T}^{-1}\) is needed for this *upper* bound: the exact Schur minimum is no larger than the energy of the explicitly chosen neighboring transition trace.

If the two exterior edge modes are still close enough for PF-343 to apply (for example with a fixed small positive transition width), that finding gives a raw mixed lower bound \(cD_n\). Subtracting the shorted mixed term (6) from the raw mixed term proves (10). The mediated Schur term absorbs the raw corridor-scale cross response.

## 3. The whole positive transition interval is dense in the corridor currency

The edge trial only handles modes next to \(\mathcal T\). The following classical completeness fact extends the **relative** \(o(D_n)\) conclusion to every bounded physical Fourier mode.

Let

\[
\mathscr H_{\rm ev}
=
L^2_{\rm even}\bigl(\mathbb R,\operatorname{sech}t\,dt\bigr)
\]

and let \(I\subset(0,\infty)\) be any nonempty open interval. Then

\[
\boxed{
\overline{\operatorname{span}}\{\cos(\xi t):\xi\in I\}
=\mathscr H_{\rm ev}.
}
\tag{16}
\]

Indeed, if an even \(f\in\mathscr H_{\rm ev}\) is orthogonal to all those cosines, consider

\[
F(z)=\int_{\mathbb R}
f(t)\operatorname{sech}t\,\cos(zt)\,dt.
\tag{17}
\]

By Cauchy--Schwarz and exponential decay of \(\operatorname{sech}t\), the integral is holomorphic on every closed substrip of \(|\operatorname{Im}z|<1/2\). It vanishes on the open real interval \(I\), hence vanishes throughout the strip by the identity theorem. Because \(f\operatorname{sech}\in L^1(\mathbb R)\) and \(f\) is even, \(F\) is its ordinary Fourier transform. Fourier uniqueness gives \(f=0\). This proves (16).

Apply (16) with \(I=(\kappa_-,\kappa_+)\). For any target frequency \(0\le\alpha\le K\) and \(\epsilon>0\), a **finite** cosine combination with frequencies strictly inside \(I\) approximates \(-\cos(\alpha t)\) in the weighted norm to accuracy \(\epsilon\). The continuous family \(\{\cos(\alpha t):0\le\alpha\le K\}\) is compact in \(\mathscr H_{\rm ev}\), so finitely many such approximants provide an \(\epsilon\)-net with a coefficient bound \(A_{\epsilon,K}<\infty\) independent of \(\alpha\). This bound need not be uniform as \(\epsilon\downarrow0\).

As \(L_n\to\infty\), the permitted discrete transition frequencies \(2\pi k/L_n\in I\) approximate the finitely many continuous frequencies in those combinations. Dominated convergence in the weighted space preserves their approximation for all sufficiently large \(n\). Therefore each \(c_{n,\xi_n}\) with \(0<\xi_n\le K\) has a transition-only compensator \(g_{n,\epsilon}\) with coefficient mass at most \(A_{\epsilon,K}\) and

\[
\int_{\mathbb R}
|\sqrt{L_n/2}(c_{n,\xi_n}+g_{n,\epsilon})(t)|^2
\operatorname{sech}t\,dt
\le C\epsilon^2.
\tag{18}
\]

Insert this compensator into (3) and use (13):

\[
0\le
\frac{\langle c_{n,\xi_n},S c_{n,\xi_n}\rangle}{D_n}
\le
C_K\epsilon^2
+
C_{\epsilon,K}\frac{1+w_n}{D_n}.
\tag{19}
\]

Take \(\limsup_{n\to\infty}\), then \(\epsilon\downarrow0\), proving (8) uniformly over the bounded target-frequency family. Positivity and Cauchy--Schwarz prove (9).

This is a form of frequency-restricted weighted approximation/superoscillation, **not** approximation in unweighted boundary \(L^2\). The compensating transition trace may have large unweighted norm. Its coefficient cost is precisely what prevents (19) from giving a quantitative trace-ideal endpoint.

## 4. Binomial transition compensators give an exponential edge rate

The neighboring-mode trial in Section 2 uses only one transition mode. Retaining a **growing but small fraction** of the transition band gives a quantitative improvement that still fits the exact positive shorting (3). The only additional arithmetic input is the Baker--Harman--Pintz prime-gap estimate already recorded as S6; there is no new spectral or superoscillation theorem.

Write \(\eta=\kappa_+-\kappa_->0\), \(h_n=2\pi/L_n\), and fix

\[
0<a<\min\left\{\frac{\eta}{8\pi},\,10^{-3}\right\},
\qquad
m_n=\lfloor a L_n\rfloor.
\tag{20}
\]

For \(n\) large, the \(m_n\) neighboring frequencies on the inside of **each** transition edge are all in the physical transition interval: the furthest displacement is at most \(m_nh_n\le 2\pi a<\eta/4\), with the single lattice-step offset at the endpoint absorbed for sufficiently large \(n\). In particular \(m_n\asymp L_n\), and no frequencies outside the actual Schur-eliminated sector are used as compensators.

For either exterior edge frequency \(\alpha_n\), take \(\sigma=+1\) at the lower edge (step upward into \(\mathcal T_n\)) and \(\sigma=-1\) at the upper edge (step downward). The normalized boundary trace whose exterior part is the selected mode and whose remaining part belongs to \(\mathcal T_n\) is

\[
\begin{aligned}
f_{n,\sigma}(t)
&=\sqrt{\frac2{L_n}}
\sum_{j=0}^{m_n}(-1)^j\binom{m_n}{j}
\cos((\alpha_n+\sigma jh_n)t)\\
&=\sqrt{\frac2{L_n}}\operatorname{Re}
\left[e^{i\alpha_nt}(1-e^{i\sigma h_nt})^{m_n}\right].
\end{aligned}
\tag{21}
\]

The coefficient absolute mass is **exactly** \(A_f=2^{m_n}\), and all frequencies are in the fixed compact physical interval \([0,\kappa_++1]\) for large \(n\). Therefore the constant in PF-344's pant/seam trial (13) is independent of \(m_n\); the coefficient cost is explicitly \(4^{m_n}\), not a hidden approximation constant.

Set \(\delta=1/(8\pi)\), so that \(2\pi\delta=1/4\). The elementary estimates

\[
|1-e^{i h_nt}|\le\min\{2,h_n|t|\},
\qquad
\operatorname{sech}t\le 2e^{-|t|}
\tag{22}
\]

give two regimes. On \(|t|\le\delta L_n\), the magnitude of the unnormalized polynomial in (21) is bounded by \(4^{-m_n}\). Outside that interval its magnitude is bounded by \(2^{m_n}\), but the exponentially decaying corridor weight absorbs that growth. Thus

\[
\boxed{
\int_{\mathbb R}
\left|\sqrt{\frac{L_n}{2}}f_{n,\sigma}(t)\right|^2
\operatorname{sech}t\,dt
\le
\pi\,16^{-m_n}+4^{m_n+1}e^{-\delta L_n}.
}
\tag{23}
\]

Inserting (23) and \(A_f=2^{m_n}\) into the actual complete-module trial (13), with the other seam modules set to zero, yields

\[
\frac{\mathcal E_M(f_{n,\sigma})}{D_n}
\le C\left(
16^{-m_n}
+4^{m_n}e^{-\delta L_n}
+\frac{(1+w_n)4^{m_n}}{D_n}
\right).
\tag{24}
\]

The last term matters: proving small weighted error alone is not enough, because binomial coefficients amplify the nonsingular pant and seam contributions.

For the *canonical prime-flute* the coefficient cost is nevertheless dominated by the corridor conductance. PF-216 and the BHP exponent \(0.525\) imply \(s_{n-1},s_n\ll p_n^{-0.475}\). The exact cuff formula in the local construction and the elementary gap lower bound \(g_n\ge2\) give \(L_n\le 2\log p_n+O(1)\). Hence

\[
\boxed{
D_n=\frac{s_{n-1}^{-1}+s_n^{-1}}{L_n}
\ge
\frac{c\,p_n^{0.475}}{L_n}
\ge\frac{c'e^{(19/80)L_n}}{L_n}.
}
\tag{25}
\]

There is no assumed prime-gap conjecture in (25). Because \(a<10^{-3}\), we have \(a\log4<\delta\) and \(a\log4<19/80\). The three terms on the right of (24) therefore decay exponentially in \(L_n\); the factor \(L_n\) from (25) can be absorbed by taking a smaller exponent. For instance any sufficiently small positive

\[
0<\gamma<
\frac12\min\left\{
a\log16,\ \delta-a\log4,\ \frac{19}{80}-a\log4
\right\}
\tag{26}
\]

works after enlarging \(C\) to account for \(m_n=\lfloor aL_n\rfloor\).

The finite-section Schur minimum (3) and positivity now give, **uniformly over canonical finite sections containing the full transition band**,

\[
\boxed{
\langle\ell_n,S\ell_n\rangle+
\langle h_n,Sh_n\rangle+
|\langle h_n,S\ell_n\rangle|
\le C D_n e^{-\gamma L_n}.
}
\tag{27}
\]

The off-diagonal bound is Cauchy--Schwarz in the **shorted** positive form, not polarization of raw pant energies. Equation (27) strengthens (5)--(7) for the same two edge modes, without changing their claim identity; it does not improve (8)--(9) for all bounded exterior modes.

**Stress tests.** If \(\eta\downarrow0\) along the tail, no fixed \(a>0\) is available and (27) does not follow. If \(D_n\) lacks a lower exponential growth rate, the nonsingular \(4^{m_n}\) term can defeat the cancellation even when the weighted integral is small. The rate is **only relative to \(D_n\)**: \(D_ne^{-\gamma L_n}\) need not tend to zero. Most importantly, no lower bound on the shorted diagonal energies is proved, so the ratio defining the normalized canonical angle may still be order one. Nothing here gives a uniform norm bound on the growing exterior bands, the unbounded high-frequency sector, finite-section compatibility, or weak-\(\mathcal S_1\) reassembly.

## Prior art and novelty assessment

The algebraic identity (3) is the classical variational meaning of a positive Schur complement/shorted form; the Dirichlet-to-Neumann setting has classical Schur-complement formulations, including Knockaert, De Zutter, Lippens and Rogier, *On the Schur complement form of the Dirichlet-to-Neumann operator*, Wave Motion 45 (2008), 309--324, DOI 10.1016/j.wavemoti.2007.07.004, already noted in PF-343.

Completeness of restricted exponential families in weighted \(L^2\) spaces is likewise classical; the general type problem and its history are treated by A. Poltoratski, *A problem on completeness of exponentials*, Annals of Mathematics 178 (2013), 983--1016, DOI 10.4007/annals.2013.178.3.4 (S21). The particular exponential-weight zero-type fact (16) is proved directly above by elementary strip analyticity, not imported as a novel theorem or as an unverified specialization of a deep result.

Finite binomial-difference identities and cancellations by repeated nearby frequencies are elementary and belong to the classical approximation/superoscillation toolkit; neither the polynomial in (21) nor the abstract Schur identity is claimed as novel. The BHP input is the established 2001 theorem recorded as S6, not an arithmetic improvement.

The project-specific delta is the transfer of these tools **through the actual PF-341 corridor variational upper trial, PF-340 zero-twist two-pant assembly, and the complete finite-section positive shorting**, with the coefficient cost beaten by the intrinsic prime-flute (D_n) scale. Neither abstract weighted completeness nor abstract Schur algebra alone implies the bounds (5)--(10) and (27) for the canonical prime flute.

## Boundaries, falsification, and remaining gate

1. **Fixed positive transition width is essential for (16)--(19).** A band with width shrinking to zero does not provide a fixed open frequency interval with the same density proof. The edge estimate (5) needs actual neighboring transition modes and can hold in a different regime only after rechecking their existence.
2. **The symmetric seam-parity geometry is essential.** The proof uses \(q_+(\xi,w_n)=O_K(w_n)\), the common zero-twist physical origin, and the positive shifted pant trial. It does not supply the analogous antisymmetric \(q_-=O(w_n^{-1})\) bound.
3. **Only bounded physical frequencies are controlled.** The complete high sector extends to arbitrarily large frequency. Neither (8) nor (9) is an operator norm bound on that whole sector.
4. **The bounds are unnormalized.** The shorted low and high diagonal energies fall at the same time as their mixed term. Dividing by them can restore order-one canonical correlation. No compactness, Schatten membership, or weak-\(\mathcal S_1\) result follows.
5. **The qualitative whole-band density proof has no conditioning rate.** Its coefficients may grow badly as the approximation error tends to zero. The binomial rate (27) solves the edge-witness coefficient-cost problem only; (19) still gives no uniform approximation rate for arbitrary bounded exterior modes or any operator bound on the growing-dimensional low band.
6. **Finite-section authority is explicit.** Every Schur inverse is taken on a strictly positive finite section containing the full relevant physical transition modes. Compatibility and ideal estimates of the infinite-tail shorted operator remain to be proved.

A decisive falsification would exhibit a failure of PF-341's noncollapsing chart extension for bounded finite cosine combinations, of the fixed-band corridor upper estimate (12), of the symmetry/normalization identification in (13), or of the strictly positive finite-section Schur minimum (3). Merely observing raw order-one correlations as in PF-343 does not contradict this shorted-form result.

The live endpoint remains quantitative beyond the edge witnesses: determine the transition-sector approximation cost for general exterior packets, then establish two-sided bounds on the **shorted** diagonal blocks and test the effective low/high angle in the PF-318/PF-320 singular-value currency. The new exponential *relative* edge rate (27) alone does not suppress the normalized angle or solve the spectral endpoint.
