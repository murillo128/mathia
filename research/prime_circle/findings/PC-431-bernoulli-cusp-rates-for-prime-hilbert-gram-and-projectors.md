# PC-431 — Bernoulli cusp asymptotics give exact rates for prime Hilbert Gram and projection limits

**Status:** EXACT-DERIVED + LITERATURE+DERIVED; quantitative refinement of PC-429's one-prime Gram limit and PC-430's strong single-prime projection limit. For every fixed \\(0<\\sigma<1\\), both the genuine Prime-Circle Hilbert--Schmidt seed and its zero-free matched control have a universal \\( (\\log p)^{-2} \\) Gram-error law and a sharp generic \\( (\\log p)^{-2} \\) *vector* projection-error law. The leading coefficient depends only on the cusp of the scalar spectral density at zero. The exponents and Bernoulli profiles survive the zero-free control and impose **no new condition on zeta zeros or RH**.

## 1. The actual cyclic spectral density

Use the multiplicity-one Hilbert--Schmidt Fourier sector from PC-427--PC-430,
\\[
\\mathcal E=L^2(\\mathbb R,(2/\\pi)|t|dt),\\qquad
(U_af)(t)=e^{iat}f(t).
\\]
For \\(j=1\\) (genuine) and \\(j=0\\) (matched zero-free control), their distinguished seeds are
\\[
g_{1,\\sigma}(t)=\\frac{\\Gamma(\\sigma-it)\\zeta(\\sigma-it)}{\\sqrt{2\\pi}},
\\qquad
g_{0,\\sigma}(t)=
-\\frac{1+\\sigma-it}{2(1-\\sigma+it)}
\\frac{\\Gamma(\\sigma-it)}{\\sqrt{2\\pi}}.
\\]
Set
\\[
w_j(t)=\\frac2\\pi|t||g_{j,\\sigma}(t)|^2
=|t|A_j(t),\\qquad M_j=\\int_\\mathbb R w_j(t)dt>0.
\\tag{1}
\\]
At each fixed \\(\\sigma\\), \\(A_j\\) is smooth and even on the real line, all its derivatives decay exponentially up to polynomial factors, and \\(A_j(0)>0\\). Explicitly,
\\[
A_1(0)=\\frac{|\\Gamma(\\sigma)\\zeta(\\sigma)|^2}{\\pi^2},
\\qquad
A_0(0)=\\frac{1}{\\pi^2}
\\left|\\frac{1+\\sigma}{2(1-\\sigma)}\\Gamma(\\sigma)\\right|^2.
\\tag{2}
\\]
There is no real zeta zero at \\(0<\\sigma<1\\): the alternating eta series is positive, while \\(1-2^{1-\\sigma}<0\\). Thus the cusp coefficients in (2) do not vanish. No assumption about nonreal zeta zeros is made.

For \\(p\\) prime, write \\(a=\\log p\\), \\(T=2\\pi/a\\), and fold the spectral measure as in PC-429:
\\[
F_{j,T}(x)=\\sum_{k\\in\\mathbb Z}w_j(x+kT),\\quad
G_{j,p}\\text{ the Gram operator of }
\\{U_{ma}g_{j,\\sigma}:m\\in\\mathbb Z\\}.
\\]
The Fourier-series model identifies \\(G_{j,p}\\) unitarily with multiplication by \\(TF_{j,T}\\) on the period-­\\(T\\) circle. Therefore
\\[
\\|G_{j,p}-M_jI\\|=\\sup_{x\\in[-T/2,T/2]}|TF_{j,T}(x)-M_j|.
\\tag{3}
\\]

## 2. Cusp-to-Bernoulli lemma and Gram rate

Here is the general analytic lemma required for both seeds. Let \\(w(t)=|t|A(t)\\), where \\(A\\) is smooth, even, positive at zero, and sufficiently rapidly decaying together with the derivatives used below. Put \\(A_*=A(0)\\), \\(M=\\int w\\), and use the Fourier transform \\(\\widehat w(\\xi)=\\int w(t)e^{-i\\xi t}dt\\).

The jump in \\(w'\\) at zero is exactly \\(2A_*\\). Twice integrating by parts separately on the positive and negative half-lines, and using the extra smooth even Taylor expansion of \\(A\\), yields
\\[
\\widehat w(\\xi)=-\\frac{2A_*}{\\xi^2}
+O(|\\xi|^{-4}),\\qquad |\\xi|\\to\\infty.
\\tag{4}
\\]
The sign comes from the Fourier transform of the cusp \\(|t|\\); an \\(O(|\\xi|^{-3})\\) term is absent because \\(A\\) is even.

Poisson periodization, valid here by integrability and absolute convergence of the sampled Fourier series, now gives uniformly in \\(x\\):
\\[
TF_T(x)-M
=\\sum_{n\\ne0}\\widehat w(na)e^{inax}
=-\\frac{4\\pi^2A_*}{a^2}
\\widetilde B_2(x/T)+O(a^{-4}),
\\tag{5}
\\]
where \\(\\widetilde B_2(y)=B_2(\\{y\\})\\) and \\(B_2(u)=u^2-u+1/6\\). In particular, \\(\\sum_{n\\ne0}e^{2\\pi inu}/n^2=2\\pi^2B_2(u)\\); thus the coefficient in (5) includes **both signs** of the Fourier frequency. Since \\(\\max_{0\\le u\\le1}|B_2(u)|=1/6\\), (3)--(5) prove
\\[
\\boxed{\\displaystyle
\\|G_{j,p}-M_jI\\|=
\\frac{2\\pi^2A_j(0)}{3(\\log p)^2}
+O((\\log p)^{-4})}.
\\tag{6}
\\]
For the genuine seed this is
\\[
\\boxed{\\displaystyle
\\lim_{p\\to\\infty}(\\log p)^2
\\|G_{1,p}-M_1I\\|=
\\frac{2|\\Gamma(\\sigma)\\zeta(\\sigma)|^2}{3}.}
\\tag{7}
\\]
PC-429 established convergence in norm, but not the nonzero leading term or its rate. The control has (6) with \\(A_0(0)\\).

## 3. Quantitative strong projector limit on smooth vectors

As in PC-430, multiplication by \\(g_{j,\\sigma}\\) is a unitary \\(J_j:L^2(w_jdt)\\to\\mathcal E\\). Let \\(Q_{j,p}\\) project \\(L^2(w_jdt)\\) onto its \\(T\\)-periodic subspace, and let \\(Q_{j,1}\\) project onto constants. For \\(f\\in C_c^\\infty(\\mathbb R)\\) put
\\[
\\mu_j(f)=M_j^{-1}\\int_\\mathbb R f(t)w_j(t)dt.
\\]
The exact weighted conditional average (PC-430) reads
\\[
(Q_{j,p}f)(x)=
\\frac{\\sum_k w_j(x+kT)f(x+kT)}
{\\sum_k w_j(x+kT)}.
\\tag{8}
\\]
The function \\(w_jf\\) has the local cusp \\(A_j(0)f(0)|t|\\); its next term can be odd, so its Fourier transform satisfies
\\[
\\widehat{w_jf}(\\xi)=
-2A_j(0)f(0)\\xi^{-2}+O(|\\xi|^{-3}).
\\]
Poisson summation applied to the numerator and (5) to the denominator of (8) therefore yields **uniformly in the periodic coordinate**:
\\[
\\boxed{\\displaystyle
(Q_{j,p}f)(x)-\\mu_j(f)
=-\\frac{4\\pi^2A_j(0)}{M_j(\\log p)^2}
\\bigl(f(0)-\\mu_j(f)\\bigr)
\\widetilde B_2(x/T)
+O_f((\\log p)^{-3}).}
\\tag{9}
\\]
Uniform positivity of the denominator for large \\(p\\) follows from \\(TF_{j,T}\\to M_j>0\\); PC-429 handles every finite prime.

As \\(T\\downarrow0\\), periodic averaging against the \\(L^1\\) density \\(w_j\\) gives
\\[
\\int_\\mathbb R
w_j(t)|\\widetilde B_2(t/T)|^2dt
\\longrightarrow
M_j\\int_0^1B_2(u)^2du=\\frac{M_j}{180}.
\\tag{10}
\\]
Writing \\(P_{j,p}=J_jQ_{j,p}J_j^{-1}\\) and \\(P_{g_j}=J_jQ_{j,1}J_j^{-1}\\), we obtain the **squared norm** limit
\\[
\\boxed{\\displaystyle
\\lim_{p\\to\\infty}(\\log p)^4
\\|(P_{j,p}-P_{g_j})(g_{j,\\sigma}f)\\|_\\mathcal E^2
=\\frac{4\\pi^4 A_j(0)^2}{45M_j}
\\left|f(0)-\\mu_j(f)\\right|^2.}
\\tag{11}
\\]
For \\(j=1\\), the coefficient is \\(4|\\Gamma(\\sigma)\\zeta(\\sigma)|^4/(45M_1)\\). Unless \\(f(0)=\\mu_j(f)\\), the **norm** error has exact order \\( (\\log p)^{-2} \\); in this exceptional case the leading term vanishes and (9) does not by itself give a universal next nonzero term. The estimate is stated for this dense smooth-vector class, not in operator norm: PC-430 proves \\(\\|P_{j,p}-P_{g_j}\\|=1\\) for every prime.

## 4. Universal control, novelty and falsification boundary

The mechanism is the generic singular spectral density \\(w(t)=|t|A(t)\\) and Fourier aliasing, not an arithmetic zero selector. The zero-free PC-424 control has \\(A_0(0)>0\\) and satisfies every formula (5)--(11). So does the entirely nonarithmetic test \\(w(t)=|t|e^{-t^2}\\), where \\(A_*=M=1\\). For the latter, direct periodization gives \\(a^2\\sup|TF_T-M|\\to 2\\pi^2/3\\), and taking \\(f(t)=e^{-t^2}\\) (a smooth rapidly decreasing extension of the compact-support test) gives \\(a^4\\|Q_pf-Q_1f\\|_{L^2(w)}^2\\to\\pi^4/45\\). These are analytic predictions; finite-grid numerical checks are corroborating controls, not proofs.

**Prior-art boundary.** Poisson summation, Euler--Maclaurin, the Fourier expansion and mean square of \\(B_2\\), and the relation between derivative jumps and inverse-square Fourier tails are classical (NIST DLMF §§24.8 and 2.10). Brandolini, Colzani, Gariboldi, Gigante and Monguzzi, *Euler--Maclaurin Summation Formula on Polytopes and Expansions in Multivariate Bernoulli Polynomials*, *J. Fourier Anal. Appl.* **29** (2023), article 33, DOI 10.1007/s00041-023-10011-9, is modern related prior art for periodized Bernoulli asymptotics; its general statements are not presented here as a zeta-specific new theorem. The Mathia-specific delta is the normalized constant and projector rate for the **actual** PC-427--PC-430 Hilbert--Schmidt spectral seeds and their matched control.

**Decisive audit tests.** Verify the \\(2/\\pi\\) Hilbert--Schmidt measure and \\(1/\\sqrt{2\\pi}\\) seed normalization in (1)--(2), the distributional jump sign in (4), the \\(2\\pi\\) periodization factor and both Fourier-frequency signs in (5), and \\(\\int_0^1B_2^2=1/180\\). Check that \\(w_jf\\) has its stated remainder (evenness is required only for the sharper \\(O(a^{-4})\\) Gram bound), that (9) is a uniform statement for **fixed** smooth \\(f\\), and that periodic averaging is applied to an integrable weight in (10). No error-rate uniformity over all unit vectors is claimed for projections. These exact rates do not exclude any off-critical zeta zero, strengthen RH, or imply a Hilbert--Pólya spectrum.
