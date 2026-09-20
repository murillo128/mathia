# WI-373 — Exact digamma dispersion sharpens the gamma negative-index profile

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + STRICT-NEGATIVE-INDEX-STRENGTHENING + SOURCE-SPECTRAL-GATE + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-371 proved that the corrected odd archimedean block reconstructed from Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* has a negative-index density at least

\[
\frac1\pi\sqrt{\frac{C_\Gamma-\eta}{M_2}}
\]

at depth `eta`, by replacing its screened nonlocal kernel by the quadratic second-moment majorant

\[
D_A[f]\le \frac{M_2}{A^2}\|f'\|_2^2.
\]

That compression loses most of the available information. Retaining the exact translation-invariant symbol of the screened kernel gives a strictly stronger depth profile, and the symbol turns out to be exactly the classical archimedean digamma multiplier from Weil's explicit formula.

Put

\[
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\qquad
h(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\]

and define

\[
d(q):=2\int_0^\infty h(s)(1-\cos qs)\,ds
\qquad(q\ge0).
\tag{1}
\]

Then

\[
\boxed{
 d(q)=\operatorname{Re}\psi\!\left(\frac14+\frac{iq}{2}\right)-\psi\!\left(\frac14\right)
}
\tag{2}
\]

and, using

\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2,
\]

one has the exact identity

\[
\boxed{
 d(q)-C_\Gamma
 =m(q):=\operatorname{Re}\psi\!\left(\frac14+\frac{iq}{2}\right)-\log\pi.
}
\tag{3}
\]

Thus the bulk dispersion of Desogus's corrected gamma block is exactly Suzuki's archimedean Weil multiplier `m`.

For every fixed

\[
0<\eta<C_\Gamma,
\]

let `q_eta>0` be the unique solution of

\[
\boxed{m(q_\eta)=-\eta,}
\tag{4}
\]

or equivalently `d(q_eta)=C_Gamma-eta`. Then the depth-`eta` negative index of WI-371 satisfies

\[
\boxed{
\liminf_{A\to\infty}\frac{\iota_\eta(\mathcal A_A)}A
\ge \frac{q_\eta}{\pi}.
}
\tag{5}
\]

At depth zero, if `q_0` denotes the unique positive zero of `m`,

\[
\boxed{
\liminf_{A\to\infty}\frac{\iota_0(\mathcal A_A)}A
\ge \frac{q_0}{\pi}.
}
\tag{6}
\]

For orientation only,

\[
q_0\approx6.28983598883690278,
\qquad
\frac{q_0}{\pi}\approx2.00211697772138498.
\tag{7}
\]

This is more than ten times WI-371's second-moment coefficient

\[
c_{\rm bulk}=0.1834951935083428577\ldots .
\]

The strengthening is strict at every nonzero depth. Since `1-cos x < x^2/2` for `x!=0`,

\[
d(q)<M_2q^2\qquad(q>0),
\tag{8}
\]

so

\[
\boxed{
\frac{q_\eta}{\pi}
>
\frac1\pi\sqrt{\frac{C_\Gamma-\eta}{M_2}}
\qquad(0<\eta<C_\Gamma).
}
\tag{9}
\]

Consequently WI-372's additive-repair spectral profile can also be sharpened exactly. If bounded self-adjoint `K_A` satisfies

\[
\mathcal A_A+K_A\succeq0,
\]

then for every `0<t<C_Gamma`,

\[
\boxed{
\liminf_{A\to\infty}\frac{N_A^+(t)}A
\ge\frac{q_t}{\pi}.
}
\tag{10}
\]

For compact `K_A`, writing its positive eigenvalues as `kappa_{A,1}>=kappa_{A,2}>=...`, every fixed

\[
0<\alpha<\frac{q_0}{\pi}
\]

obeys the exact quantile envelope

\[
\boxed{
\liminf_{A\to\infty}
\kappa_{A,\lceil\alpha A\rceil}
\ge -m(\pi\alpha).
}
\tag{11}
\]

If `K_A` belongs to `S_p`, `1<=p<infinity`, then

\[
\boxed{
\liminf_{A\to\infty}A^{-1/p}\|K_A\|_{\mathfrak S_p}
\ge
\Theta_p,
\qquad
\Theta_p^p=
\frac1\pi\int_0^{q_0}[-m(q)]^p\,dq.
}
\tag{12}
\]

For orientation, `Theta_1≈2.24788711864` and `Theta_2≈2.35761383938`, compared with WI-372's second-moment values `tau_1≈0.65718` and `tau_2≈1.68059`.

If the additive repair factors as `K_A=B_A^*B_A`, equation (11) gives the corresponding exact singular-value gate

\[
\boxed{
\liminf_{A\to\infty}
 s_{\lceil\alpha A\rceil}(B_A)
\ge \sqrt{-m(\pi\alpha)}
\qquad
\left(0<\alpha<\frac{q_0}{\pi}\right).
}
\tag{13}
\]

As in WI-371--WI-372, none of these statements says that Desogus's actual common-cut/rooted-Schur source network is a bounded additive or factorized repair. They are necessary gates for such a reduction and a quantitative description of the corrected gamma block itself, not a refutation of Gate II and not evidence against RH.

## 1. Exact whole-line symbol of the screened difference form

WI-369 reconstructs the positive remainder in

\[
\mathcal A_A+C_\Gamma I=R_A\succeq0
\]

as the sum of a screened difference form `D_A`, a positive endpoint multiplier and a positive Hankel image. The screened term is

\[
D_A[f]
=\frac A2\iint_{(0,1)^2}
 h(A|u-v|)|f(u)-f(v)|^2\,du\,dv.
\tag{14}
\]

Let `f` be supported in a fixed interior interval and extend it by zero to the real line. Adding the missing exterior pairs can only increase the nonnegative difference energy, so

\[
D_A[f]\le\widetilde D_A[f],
\tag{15}
\]

where

\[
\widetilde D_A[f]
:=\frac A2\iint_{\mathbb R^2}
 h(A|u-v|)|f(u)-f(v)|^2\,du\,dv.
\tag{16}
\]

With Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-i\xi u}\,du,
\]

translation invariance and Parseval give exactly

\[
\boxed{
\widetilde D_A[f]
=\frac1{2\pi}\int_{\mathbb R}
 d(\xi/A)|\widehat f(\xi)|^2\,d\xi.
}
\tag{17}
\]

The integral in (1) can be evaluated termwise because

\[
h(s)=\sum_{n\ge0}e^{-(2n+1/2)s}
\]

and every summand in `(1)` is nonnegative. Writing `x_n=n+1/4`,

\[
\begin{aligned}
d(q)
&=2\sum_{n\ge0}
\frac{q^2}{(2n+1/2)((2n+1/2)^2+q^2)}\\
&=\sum_{n\ge0}
\frac{q^2}{x_n(4x_n^2+q^2)}.
\end{aligned}
\tag{18}
\]

The standard digamma difference identity

\[
\psi(z)-\psi(a)
=\sum_{n\ge0}
\left(\frac1{n+a}-\frac1{n+z}\right)
\]

now gives (2) exactly. Equation (3) follows from the classical special value of `psi(1/4)`.

This identity is also a normalization stress test. The corrected bulk symbol extracted from Desogus's physical-space gamma kernel reproduces precisely the archimedean multiplier `m` in Suzuki's source-exact Fourier formula, with no residual scalar.

## 2. Concavity retains the exact symbol on a Dirichlet band

The key point is that the exact symbol can be controlled by the same first-derivative Rayleigh quotient used in WI-371 without replacing it by its quadratic Taylor majorant. Put

\[
F(y):=d(\sqrt y)
=\sum_{n\ge0}
\frac{y}{x_n(4x_n^2+y)},
\qquad y\ge0.
\tag{19}
\]

Every summand is increasing and concave in `y`; explicitly,

\[
\frac{d}{dy}
\frac{y}{x(4x^2+y)}
=\frac{4x}{(4x^2+y)^2}>0,
\]

and

\[
\frac{d^2}{dy^2}
\frac{y}{x(4x^2+y)}
=-\frac{8x}{(4x^2+y)^3}<0.
\]

Thus `F` is increasing and concave. Normalize the Fourier power of a nonzero `f` to the probability measure

\[
d\mu_f(\xi)
=\frac{|\widehat f(\xi)|^2}{2\pi\|f\|_2^2}\,d\xi.
\]

Equations (15)--(17) and Jensen's inequality give the exact deterministic majorant

\[
\begin{aligned}
\frac{D_A[f]}{\|f\|_2^2}
&\le\int F(\xi^2/A^2)\,d\mu_f(\xi)\\
&\le F\!\left(
\frac1{A^2}\int\xi^2\,d\mu_f(\xi)
\right)\\
&=
\boxed{
 d\!\left(\frac{\|f'\|_2}{A\|f\|_2}\right).
}
\end{aligned}
\tag{20}
\]

The second-moment estimate of WI-371 is recovered by applying `d(q)<=M_2q^2` to (20). Hence (20) is a strict retention of the information that WI-371 explicitly identified as its remaining kernel slack.

## 3. Exact depth-resolved negative-index density

Fix `0<delta<1/2` and set

\[
I_\delta=(\delta,1-\delta),
\qquad
L_\delta=1-2\delta.
\]

WI-371 already proves that on functions supported in `I_delta`, the positive endpoint and Hankel pieces of `R_A` contribute at most

\[
\varepsilon_A(\delta)
=2H(A\delta)+A L_\delta h(2A\delta)
\longrightarrow0
\tag{21}
\]

times `||f||_2^2`.

Use the first `m` Dirichlet modes on `I_delta`, with the same finite-dimensional `C_c^infty(I_delta)` approximation used in WI-371. Their maximal derivative Rayleigh quotient is arbitrarily close to

\[
\left(\frac{m\pi}{L_\delta}\right)^2.
\tag{22}
\]

Fix `0<eta<C_Gamma` and choose

\[
c<\frac{L_\delta q_\eta}{\pi}.
\tag{23}
\]

For `m_A=floor(cA)`, equations (20)--(23), continuity and strict monotonicity of `d`, and `epsilon_A(delta)->0` give a fixed positive margin for all sufficiently large `A`:

\[
R_A[f]
\le(C_\Gamma-\eta-\mu)\|f\|_2^2
\]

on an `m_A`-dimensional core subspace. Since

\[
\mathcal A_A=-C_\Gamma I+R_A,
\]

that whole subspace lies below depth `-eta`. Therefore

\[
\liminf_{A\to\infty}\frac{\iota_\eta(\mathcal A_A)}A
\ge\frac{L_\delta q_\eta}{\pi}.
\]

Letting `delta` decrease to zero proves (5).

WI-295 independently proves that the exact multiplier `m(q)` is strictly increasing for `q>0`; alternatively this follows directly by differentiating the trigamma series. Since

\[
m(0)=-C_\Gamma<0,
\qquad
m(q)\to+\infty
\quad(q\to\infty),
\]

`q_eta` and `q_0` are unique. Letting `eta` decrease to zero in (5) proves (6).

The strict comparison (9) follows directly from (1): for `q>0`, `h(s)>0` and `1-cos(qs)<q^2s^2/2` except on a null discrete set, hence

\[
d(q)<q^2\int_0^\infty s^2h(s)\,ds=M_2q^2.
\]

Thus the new profile strictly improves WI-371 at every depth, not only at the zero-depth endpoint.

## 4. Exact repair spectral envelope

WI-372's min--max argument applies verbatim with (5) in place of the parabolic depth profile. If `A_A+K_A` is nonnegative, every depth-`t` negative subspace for `A_A` forces at least the same number of eigenvalues of `K_A` to be at least `t`. This proves (10).

To invert the count, fix

\[
0<\alpha<q_0/\pi.
\]

For every

\[
0<t<-m(\pi\alpha),
\]

strict monotonicity of `m` gives `q_t>pi alpha`, so (10) forces at least `alpha A+o(A)` positive eigenvalues at level `t`. Letting `t` increase to `-m(pi alpha)` gives (11).

For the Schatten profile, the layer-cake identity and Fatou's lemma give

\[
\liminf_{A\to\infty}
\frac{\|K_A\|_{\mathfrak S_p}^p}{A}
\ge
\frac p\pi\int_0^{C_\Gamma}t^{p-1}q_t\,dt.
\tag{24}
\]

Substitute `t=-m(q)`. Since `m(q_0)=0` and `m(0)=-C_Gamma`, integration by parts yields exactly

\[
\frac p\pi\int_0^{C_\Gamma}t^{p-1}q_t\,dt
=
\frac1\pi\int_0^{q_0}[-m(q)]^p\,dq,
\]

which is (12). Equation (13) follows from the squared singular-value/eigenvalue identity for `B_A^*B_A`.

Because (8) is strict for every positive `q`, the digamma quantile envelope `-m(pi alpha)=C_Gamma-d(pi alpha)` lies strictly above WI-372's parabolic envelope

\[
C_\Gamma-\pi^2M_2\alpha^2
\]

throughout their common positive range. The gain is therefore structural, not just a better numerical evaluation of the same bound.

## 5. Prior-art and novelty audit

The load-bearing identities separate cleanly.

- **Suzuki / classical explicit formula:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, gives the exact archimedean Fourier multiplier `m(q)=Re psi(1/4+iq/2)-log pi` in the localized Weil form. The digamma difference identity and the special value of `psi(1/4)` are classical.
- **Desogus primary source:** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, gives the transported Cauchy--Carleman/gamma kernels whose parity-corrected reconstruction in WI-364 and WI-369 produces the screened kernel `h`. The preprint itself claims cancellation of the regular gamma kernel; WI-364 identifies the omitted parity image, and WI-369 reconstructs the corrected positive remainder and floor. The present finding does not import the claimed RH proof.
- **Local antecedents:** WI-240 records Suzuki's exact multiplier and proves only unbounded prime-deleted odd negative index by fixed-dimensional low-frequency dilation. WI-295 proves strict radial monotonicity of the same digamma multiplier in a screened-support problem. WI-371 proves a linear negative-index density for the corrected Desogus gamma block but explicitly identifies its replacement `D_A<=M_2 A^{-2}||f'||^2` as the remaining kernel slack. WI-372 converts that parabolic depth law into a repair eigenvalue/Schatten profile.

A targeted search of the local `weil_inertia` corpus found no existing result identifying the exact Desogus screened-difference bulk symbol with Suzuki's multiplier, no previous coefficient `q_0/pi`, and no digamma repair quantile law (11). Web searches around the recent Desogus and Suzuki papers located the standard Weil digamma multiplier and numerical Archimedean spectral work, but no matching negative-index density or repair-profile theorem. Search absence is not a priority claim.

## 6. Validation boundary and research consequence

Equations (1)--(6) are exact consequences of the already reconstructed corrected gamma block plus Fourier/concavity estimates; no interval certificate, unproved zero statistic, or RH assumption enters. The decimals in (7) and after (12) are non-load-bearing orientation only.

The theorem still concerns the corrected **archimedean gamma block** and additive/factorized repairs of that block. Desogus's actual common-cut/rooted-Schur architecture is a source-conditioned, nontrivial Schur mechanism and is not asserted to reduce to such a repair with uniformly bounded weight. Therefore this is a sharper audit gate, not a disproof of the preprint.

The practical source-side target changes substantially. WI-372 required an additive repair to carry only `0.18349 A+o(A)` nontrivial directions at vanishing depth. The exact kernel forces at least

\[
\boxed{2.00211 A+o(A)}
\]

positive repair directions in the zero-depth limit, with strengths following the full curve `-m(pi alpha)`. Any attempt to validate the Desogus source mechanism by collapsing it to a bounded additive/factorized correction must now demonstrate this much denser coupling profile. Conversely, a successful audit of the true common-cut/rooted-Schur mechanism may evade the gate precisely because it changes the effective geometry rather than acting as an after-the-fact additive repair.