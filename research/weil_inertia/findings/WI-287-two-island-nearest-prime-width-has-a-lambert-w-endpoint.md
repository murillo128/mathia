# WI-287 — the two-island nearest-prime width interface has a Lambert-W endpoint

## Status

- **Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened, symmetric two-island** branch of `WI-284`--`WI-286`, after compressing the aperture-growing prime family to the single nearest-prime width consequence. This finding sharpens `WI-286` inside that deliberately compressed interface; it does not replace the full screening constraints.
- **Result:** the apparent exponent-only transition `theta=1/2` from `WI-286` has a sharp logarithmic refinement. If a prime-in-short-interval input has length

  \[
  H(x)=\sqrt{x}\,F(x),
  \]

  with `F(x) -> infinity` and `F(x)=O(log x)`, then the bottom of the **nearest-prime width relaxation** of the prime-deleted form is

  \[
  \boxed{
  \lambda_{\rm width}(x)
  =\frac12\log x-\log F(x)-F(x)+O(1).
  }
  \]

  Hence the sign transition lies, up to a bounded additive window in `F`, at

  \[
  \boxed{
  F_*(x)=W(\sqrt{x})
  =\frac12\log x-\log\log x+\log2+o(1),
  }
  \]

  where `W` is Lambert's `W` function. In particular a uniform prime interval theorem with `H(x)=sqrt(x)F(x)` and `F(x) <= W(sqrt(x))-omega(x)`, `omega(x)->infinity`, would force the entire prime-deleted form on every such completely screened two-island support to be strictly positive; while if `F(x) >= W(sqrt(x))+omega(x)`, the width relaxation itself still contains explicit odd directions with Rayleigh quotient tending to `-infinity`.
- **What it does not claim:** the negative half constructs profiles satisfying only the scalar width constraint extracted from the nearest prime; it does **not** construct a support screening all actual prime-power lags. The positive half rules out only symmetric two-island completely screened supports. It does not handle many-component supports, sign-changing first modes, incomplete screening, or the full `WI-284` contradiction. No unconditional prime-gap theorem currently reaches the positive Lambert-`W` side.
- **Novelty boundary:** the prime-deleted gamma/pole decomposition is Suzuki's and was already source-audited in `WI-240`; Cramer-type `sqrt(x) log x` prime intervals under RH are classical and have optimized modern constants. The new line-local deductions are (i) the sharp support-measure lower bound for the logarithmic gamma energy obtained from the Fourier `L^infinity` cap, (ii) the exact negative eigenvalue of Suzuki's rank-two pole form on a symmetric two-island support, and (iii) their combination into the Lambert-`W` endpoint for the nearest-prime width relaxation. Targeted prior-art searches found the prime-gap and Weil-form ingredients but not this combined support-spectral threshold. Search absence is audit context only, not a priority claim.

## Claim

Retain the symmetric two-island geometry of `WI-286`,

\[
E_{R,b}
:=(-R-b,-R+b)\cup(R-b,R+b),
\qquad R> b>0,
\tag{1}
\]

and put

\[
\Delta:=2R,
\qquad
x:=e^\Delta=e^{2R}.
\tag{2}
\]

Let `q_arch^a=G+P_a` be Suzuki's exact prime-deleted gamma-plus-pole form on aperture `a=R+b`. Suppose an arithmetic input guarantees, for every sufficiently large `x`, a prime in

\[
[x,x+H(x)]
\tag{3}
\]

with `H(x)=o(x)`. Complete screening then forces the necessary width constraint from `WI-286`,

\[
2b\le \log\!\left(1+\frac{H(x)}x\right).
\tag{4}
\]

Define

\[
F(x):=\frac{H(x)}{\sqrt{x}},
\qquad
b_c(x):=\frac12\log\!\left(1+F(x)x^{-1/2}\right),
\tag{5}
\]

and define the width-relaxed spectral bottom

\[
\lambda_{\rm width}(x)
:=
\inf_{0<b\le b_c(x)}
\inf_{0\ne u\in\mathfrak D(q_{\rm arch}^a)\cap L^2(E_{R,b})}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}.
\tag{6}
\]

This is intentionally weaker than complete screening: it retains only the consequence (4) of the growing prime family.

If

\[
F(x)\to\infty,
\qquad
F(x)=O(\log x),
\tag{7}
\]

then

\[
\boxed{
\lambda_{\rm width}(x)
=rac12\log x-\log F(x)-F(x)+O(1).
}
\tag{8}
\]

Consequently, writing

\[
F_*(x):=W(\sqrt{x}),
\tag{9}
\]

so that

\[
F_*(x)+\log F_*(x)=\frac12\log x,
\tag{10}
\]

we have for every `omega(x)->infinity`:

\[
F(x)\le F_*(x)-\omega(x)
\quad\Longrightarrow\quad
\lambda_{\rm width}(x)\to+\infty,
\tag{11}
\]

whereas

\[
F(x)\ge F_*(x)+\omega(x)
\quad\Longrightarrow\quad
\lambda_{\rm width}(x)\to-\infty.
\tag{12}
\]

The standard Lambert-`W` expansion gives

\[
\boxed{
F_*(x)
=\frac12\log x-\log\log x+\log2+o(1).
}
\tag{13}
\]

Thus the nearest-prime width interface is not merely separated by the power exponent `1/2`; at square-root scale its transition is located to second order at

\[
\boxed{
H_*(x)
=\sqrt{x}\left(
\frac12\log x-\log\log x+O(1)
\right).
}
\tag{14}
\]

The bounded `O(1)` window in (14) is real at the level of the present argument: pinning its constant would require the exact bottom constant for the gamma form on the shrinking two-island support rather than only uniform upper/lower constants.

## 1. A bathtub bound recovers the full logarithmic gamma cost

`WI-286` used a half-Fourier-mass argument and obtained only

\[
G(u)/\|u\|_2^2
\ge \frac12\log(1/b)-O(1).
\tag{15}
\]

That loses a factor two. The support itself gives the sharp logarithmic coefficient without any external uncertainty theorem.

Let `E` be any measurable set of finite measure `mu`, and let `u` be supported in `E`. With the Fourier normalization of `WI-240` and `WI-286`,

\[
\frac1{2\pi}\int_{\mathbb R}|\widehat u(z)|^2\,dz=\|u\|_2^2.
\tag{16}
\]

Cauchy--Schwarz gives

\[
|\widehat u(z)|^2
\le \|u\|_1^2
\le \mu\,\|u\|_2^2.
\tag{17}
\]

Therefore

\[
p_u(z):=\frac{|\widehat u(z)|^2}{2\pi\|u\|_2^2}
\tag{18}
\]

is a probability density satisfying

\[
0\le p_u(z)\le \frac\mu{2\pi}.
\tag{19}
\]

Among probability densities with the pointwise cap (19), the integral of the even increasing function `log(1+|z|)` is minimized by saturating the cap on the centered interval of the smallest permitted length. This elementary bathtub rearrangement gives

\[
\int \log(1+|z|)p_u(z)\,dz
\ge
\frac\mu\pi
\int_0^{\pi/\mu}\log(1+z)\,dz.
\tag{20}
\]

Writing

\[
B(t):=\frac{(1+t)\log(1+t)-t}{t}
=\left(1+\frac1t\right)\log(1+t)-1,
\tag{21}
\]

this is

\[
\int \log(1+|z|)p_u(z)\,dz
\ge B(\pi/\mu).
\tag{22}
\]

For all `t>0`,

\[
B(t)\ge\log t-1.
\tag{23}
\]

Suzuki's gamma multiplier is

\[
m(z)=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi.
\tag{24}
\]

By continuity and the standard vertical-line digamma asymptotic, there is an absolute `C_Gamma` such that

\[
m(z)\ge\log(1+|z|)-C_\Gamma
\qquad(z\in\mathbb R).
\tag{25}
\]

Combining (22)--(25),

\[
\boxed{
\frac{G(u)}{\|u\|_2^2}
\ge
B(\pi/\mu)-C_\Gamma
\ge
\log\frac1\mu-C_0.
}
\tag{26}
\]

For `E=E_{R,b}`, `mu=4b`, so

\[
\boxed{
G(u)/\|u\|_2^2
\ge \log(1/b)-C_1.
}
\tag{27}
\]

The coefficient of `log(1/b)` is now one, and it is sharp: a rescaled fixed compact profile has gamma energy `log(1/b)+O(1)`.

## 2. The pole form has an exact negative eigenvalue on two symmetric islands

`WI-286` bounded the pole term by absolute values. On a symmetric support its negative spectral edge can be diagonalized exactly.

Put

\[
a_-(t):=e^{-t/2}\mathbf1_{E_{R,b}}(t),
\qquad
a_+(t):=e^{t/2}\mathbf1_{E_{R,b}}(t).
\tag{28}
\]

For general complex `u` supported in `E_{R,b}`, Suzuki's pole factorization is

\[
P_a(u)=2\operatorname{Re}
\left(
\langle u,a_-\rangle
\overline{\langle u,a_+\rangle}
\right).
\tag{29}
\]

The corresponding rank-two self-adjoint operator has eigenvectors `a_-+a_+` and `a_--a_+`. Symmetry gives

\[
\|a_-\|_2^2=\|a_+\|_2^2
=4\sinh(b)\cosh(R),
\tag{30}
\]

and

\[
\langle a_-,a_+\rangle=|E_{R,b}|=4b.
\tag{31}
\]

Hence its two nonzero eigenvalues are

\[
4b+4\sinh(b)\cosh(R)
\tag{32}
\]

and

\[
4b-4\sinh(b)\cosh(R).
\tag{33}
\]

Therefore every supported vector satisfies the exact lower bound

\[
\boxed{
\frac{P_a(u)}{\|u\|_2^2}
\ge
-4\bigl(\sinh(b)\cosh(R)-b\bigr).
}
\tag{34}
\]

This replaces the factor-two-weaker absolute estimate from `WI-286`.

Now impose the nearest-prime width cap `b<=b_c`. If

\[
t:=F(x)x^{-1/2},
\qquad
b_c=\frac12\log(1+t),
\tag{35}
\]

then the identity

\[
\sinh(b_c)=\frac{t}{2\sqrt{1+t}}
\tag{36}
\]

and

\[
\cosh(R)=\frac{\sqrt{x}+1/\sqrt{x}}2
\tag{37}
\]

give

\[
4\sinh(b_c)\cosh(R)
=
\frac{F(x)(1+x^{-1})}{\sqrt{1+F(x)x^{-1/2}}}
\le F(x)(1+x^{-1}).
\tag{38}
\]

Since the left side of (34) worsens monotonically with `b`, equations (34) and (38) imply, uniformly for all admissible `b`,

\[
\boxed{
P_a(u)/\|u\|_2^2
\ge -F(x)-o(1)
}
\tag{39}
\]

in the endpoint regime (7).

## 3. Uniform lower bound for the whole width relaxation

From (4)--(5),

\[
b\le b_c
\le\frac{F(x)}{2\sqrt{x}},
\tag{40}
\]

so

\[
\log\frac1b
\ge
\frac12\log x-\log F(x)+\log2.
\tag{41}
\]

Combining (27), (39), and (41) gives

\[
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}
\ge
\frac12\log x-\log F(x)-F(x)-C_2-o(1)
\tag{42}
\]

for every admissible two-island width and every nonzero supported form-domain vector. Therefore

\[
\boxed{
\lambda_{\rm width}(x)
\ge
\frac12\log x-\log F(x)-F(x)-O(1).
}
\tag{43}
\]

This already proves the positive half of the transition.

## 4. A flat odd vector matches the lower bound to `O(1)`

The converse does not require a delicate smooth near-extremizer. The signed indicator of the two islands is already in the prime-deleted form domain: its Fourier transform decays as `O(1/|z|)`, so the logarithmically weighted gamma integral converges.

Take the maximal width

\[
b=b_c(x)
\tag{44}
\]

and define

\[
u_{R,b}
:=
\mathbf1_{(R-b,R+b)}
-
\mathbf1_{(-R-b,-R+b)}.
\tag{45}
\]

Its norm is

\[
\|u_{R,b}\|_2^2=4b.
\tag{46}
\]

For this odd vector the pole identity gives exactly

\[
\frac{P_a(u_{R,b})}{\|u_{R,b}\|_2^2}
=
-\frac{32}{b}
\sinh^2(b/2)\sinh^2(R/2).
\tag{47}
\]

Under (7), `b=O((log x)/sqrt(x))`, and therefore

\[
\frac{P_a(u_{R,b})}{\|u_{R,b}\|_2^2}
=-2b\sqrt{x}+o(1)
=-F(x)+o(1).
\tag{48}
\]

For the gamma term, the global digamma upper bound gives

\[
m(z)\le\log(1+|z|)+C_3.
\tag{49}
\]

Moreover

\[
\widehat{u_{R,b}}(z)
=4i\,\frac{\sin(Rz)\sin(bz)}{z}
\tag{50}
\]

up to an irrelevant sign. After the change `t=bz`, split

\[
\log(1+|t|/b)
=
\log(1/b)+\log(b+|t|).
\tag{51}
\]

The constant term integrates to exactly `log(1/b)` after division by the norm, by Parseval. Since `b<=1`, the remainder is bounded above by the integrable weight

\[
\log(1+|t|)\frac{\sin^2 t}{t^2},
\tag{52}
\]

independently of `R/b`. Hence

\[
\boxed{
G(u_{R,b})/\|u_{R,b}\|_2^2
\le\log(1/b)+C_4.
}
\tag{53}
\]

Finally, from (35) and `F=O(log x)`,

\[
\log(1/b_c)
=
\frac12\log x-\log F(x)+O(1).
\tag{54}
\]

Equations (48), (53), and (54) give

\[
\boxed{
\lambda_{\rm width}(x)
\le
\frac12\log x-\log F(x)-F(x)+O(1).
}
\tag{55}
\]

Together with (43), this proves (8).

The witness in this section is only a width-relaxation witness. It is **not** asserted to avoid every actual prime-power lag. That distinction is the same decisive distinction made in `WI-286` between a barrier for the compressed nearest-prime interface and a counterexample to complete screening.

## 5. Lambert `W` is the exact asymptotic transition variable

Let

\[
\Xi_x(F)
:=
\frac12\log x-\log F-F.
\tag{56}
\]

Equation (8) says that the relaxed spectral bottom is `Xi_x(F)+O(1)`. The unique positive root of `Xi_x(F)=0` satisfies

\[
F+\log F=\frac12\log x,
\tag{57}
\]

or equivalently

\[
F e^F=\sqrt{x}.
\tag{58}
\]

Thus

\[
F=F_*(x)=W(\sqrt{x}).
\tag{59}
\]

Since `d(F+log F)/dF=1+1/F`, a displacement tending to infinity on either side of `F_*` forces `Xi_x(F)` to tend to the opposite infinity. This proves (11)--(12).

The standard asymptotic expansion

\[
W(y)=\log y-\log\log y+o(1)
\tag{60}
\]

with `y=sqrt(x)` yields (13). In particular:

- any `H(x)=o(sqrt(x) log x)` lies safely on the positive side once `F` is in the growing endpoint regime;
- more sharply, `H(x)=sqrt(x)(c log x)` is sufficient through this interface for every fixed `c<1/2`;
- every fixed `c>1/2` is decisively on the negative-relaxation side;
- the nominal constant `c=1/2` is itself above the second-order transition because the missing `-log log x` term matters. Width-only control at `H=(1/2)sqrt(x)log x` still admits negative Rayleigh quotients tending to `-infinity`.

So the correct endpoint currency is not just the power `theta-1/2`; it is

\[
\boxed{
F+\log F-\frac12\log x.
}
\tag{61}
\]

## 6. Prior-art and current-input audit

The load-bearing spectral identities are the exact Suzuki prime-deleted decomposition already audited in `WI-240` and reused in `WI-284`--`WI-286`:

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), https://arxiv.org/abs/2606.09096.

The nearest-prime input in `WI-286` used the peer-reviewed unconditional theorem

- R. C. Baker, G. Harman and J. Pintz, **The difference between consecutive primes, II**, *Proc. London Math. Soc.* 83:3 (2001), 532--562, DOI `10.1112/plms/83.3.532`, giving the exponent `0.525`.

The current literature audit also finds Runbo Li, **The number of primes in short intervals and numerical calculations for Harman's sieve**, arXiv:2308.04458v8 (2025), https://arxiv.org/abs/2308.04458, which claims the stronger unconditional exponent `0.52`. This remains an unrefereed preprint and is therefore not promoted to the peer-reviewed established tier. Either exponent is far on the negative side of the present endpoint: it corresponds to `F=x^0.025` or `F=x^0.02`, respectively, rather than `F~(1/2)log x`.

For calibration only, the classical RH-conditional Cramer scale is exactly the scale resolved here. Adrian Dudek, **On the Riemann Hypothesis and the Difference Between Primes**, *International Journal of Number Theory* 10 (2014), 905--911; arXiv:1402.6417, proves under RH a prime in `(x-(4/pi)sqrt(x)log x,x]` for every `x>=2`, with `4/pi` reducible to `1+epsilon` for sufficiently large `x`. Carneiro--Milinovich--Soundararajan, **Fourier optimization and prime gaps**, *Comment. Math. Helv.* 94 (2019), 533--568, DOI `10.4171/CMH/467`, sharpen the Cramer-type constant framework, and Chirre--Pereira Júnior--de Laat, **Primes in arithmetic progressions and semidefinite programming**, *Math. Comp.* 90 (2021), 2235--2246, DOI `10.1090/mcom/3638`, report the ordinary-prime constant `0.8358` in this line of work. These conditional constants remain above the leading `1/2` threshold of the nearest-prime width interface. This is only a scale comparison: RH is not used as evidence in the present unconditional program.

Cramer's much stronger conjectural maximal-gap scale `O(log^2 x)` would lie deep on the positive side, but it is conjectural and is not used.

Targeted searches around Suzuki/Weil quadratic forms, prime gaps, Cramer-type short intervals, and `sqrt(x) log x` support uncertainty located the ingredients above but no prior statement of (8), the exact rank-two support pole edge (34) in this screening context, or the Lambert-`W` transition (59). No priority claim is made.

## 7. Research consequence

`WI-286` correctly identified the square-root exponent as the first transition, but its half-mass gamma estimate and absolute pole estimate deliberately left the endpoint unresolved. The two exact refinements above remove that slack inside the same compressed interface. The resulting barrier is now sharp up to a bounded additive uncertainty in `F=H/sqrt(x)`:

\[
\boxed{
H_*(x)
=\sqrt{x}\,W(\sqrt{x})
=\sqrt{x}\left(
\frac12\log x-\log\log x+O(1)
\right).
}
\tag{62}
\]

This materially changes what a nearest-prime-only rescue would have to deliver. Merely reaching a square-root exponent, or even a generic `C sqrt(x) log x` theorem, is not enough: the constant and then the `log log x` correction matter. The known unconditional inputs are vastly too weak, and even the standard RH-conditional Cramer-type constants sit on the wrong side of this compressed spectral threshold.

Therefore further unconditional work should **not** spend effort trying to improve `0.52` or `0.525` incrementally inside the nearest-prime reduction. The viable source-specific information is precisely what that reduction discards: simultaneous action of many prime lags, their positive von-Mangoldt amplitudes in the null equation, or multi-component geometry. Those are the mechanisms capable of beating the Lambert-`W` width barrier without asking for an unrealistically strong pointwise prime-gap theorem as a side effect.