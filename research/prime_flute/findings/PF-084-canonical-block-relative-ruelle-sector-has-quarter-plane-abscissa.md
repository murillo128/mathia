# PF-084 — the canonical all-block exact/reference Ruelle sector has abscissa 1/4

**Status:** `POSITIVE-CANONICAL-RELATIVE-SECTOR` + `EXACT-ABSCISSA` for the Euler-product region of absolute convergence. This is **not** a full Ruelle zeta of the infinite flute and is **not** a claim about RH. It is a nonlocal extension of PF-083 from adjacent four-prime separators to every canonical finite consecutive cusp block.

PF-083 showed that the exact prime-circle endpoint map

\[
V(p)=\pi\cot\frac{\pi}{p}
\]

and its projective tangent reference

\[
V_0(p)=p
\]

are close enough that the relative Ruelle product for the nearest period-two separator family converges and is nonzero on all of `Re s > 0`.

PF-042 supplies a much larger, still canonical, family. If

\[
G_j=G(u_{j-1},u_j)
\]

are the exact adjacent side-pairings, then the loop around every finite consecutive cusp block telescopes to

\[
G_mG_{n+1}^{-1}.
\]

It is a primitive simple separating geodesic. Thus the ordered flute topology itself selects a two-parameter family indexed by intervals `m..n`; no arbitrary orbit selection or gap-generated weight is introduced.

The main result is

\[
\boxed{
\mathcal R_{\rm rel}^{\rm block}(s)
=
\prod_{m<n}
\frac{1-e^{-sL^E_{m,n}}}
     {1-e^{-sL^0_{m,n}}}
}
\]

where `E` denotes the exact `V(p)` geometry and `0` the projective-reference `p` geometry. This product converges locally uniformly and to a nonzero holomorphic function on

\[
\boxed{\operatorname{Re}s>\frac14,}
\]

while its logarithmic series fails to converge absolutely for

\[
\boxed{0<\operatorname{Re}s\le\frac14.}
\]

For real `s=1/4`, already the subproduct obtained by fixing one left endpoint block has logarithm tending to `-infinity`, so the ordinary nonzero Euler product fails exactly at the boundary.

The appearance of `1/4` is caused by a nonlocal coupling of the two end gaps/cuffs of a long block; it is not imported from the Riemann critical line or from modular scattering.

## 1. Exact block separator and cross-ratio

Fix indices `m<n` and put, in the linear reference geometry,

\[
a=p_{m-1},\qquad b=p_m,\qquad c=p_n,\qquad d=p_{n+1}.
\]

Write

\[
X=b-a,\qquad Y=c-b,\qquad Z=d-c.
\]

The canonical simple block separator has

\[
\boxed{
\sinh^2\frac{L^0_{m,n}}4
=\chi^0_{m,n}
=\frac{(c-b)(d-a)}{(b-a)(d-c)}
=\frac{Y(X+Y+Z)}{XZ}.
}
\]

The exact prime-circle length uses the same formula after applying `V` to all four endpoints:

\[
\chi^E_{m,n}
=
\frac{(V(c)-V(b))(V(d)-V(a))}
     {(V(b)-V(a))(V(d)-V(c))},
\]

\[
L^{E,0}_{m,n}=4\operatorname{arsinh}\sqrt{\chi^{E,0}_{m,n}}.
\]

Because these are cross-ratios, the statement is invariant under the Möbius conjugacies used in the exact orthogonal-circle model. The ambient interior/exterior involution therefore gives the conjugate same relative sector, not a second independent zeta channel.

## 2. Uniform exact/reference projective defect

Define the divided difference

\[
D_V(x,y)=\frac{V(y)-V(x)}{y-x}.
\]

PF-083 gives

\[
V'(x)=\left(\frac{\pi/x}{\sin(\pi/x)}\right)^2,
\qquad
\log V'(x)=O(x^{-2}).
\]

By the mean value theorem,

\[
\log D_V(x,y)=O(x^{-2})
\]

uniformly for `y>x`. Hence

\[
\frac{\chi^E_{m,n}}{\chi^0_{m,n}}
=
\frac{D_V(b,c)D_V(a,d)}
     {D_V(a,b)D_V(c,d)}
\]

and, using Bertrand to compare `a` and `b`,

\[
\boxed{
\delta u_{m,n}
:=\log\frac{\chi^E_{m,n}}{\chi^0_{m,n}}
=O(p_m^{-2})
}
\]

uniformly in the right endpoint `n`.

This is crucial: moving the far endpoint arbitrarily far does not amplify the finite-scale projective defect at the left end.

## 3. Relative Ruelle logarithm gains exponential block decay

For `Re s>0` let

\[
f_s(L)=\log(1-e^{-sL}).
\]

With `u=log chi` and `L=4 asinh(e^{u/2})`,

\[
\frac{d}{du}f_s(L(u))
=
\frac{2s\tanh(L/4)}{e^{sL}-1}.
\]

For every compact `K` in `Re s >= sigma > 0`, this derivative is bounded for small `L` and satisfies

\[
\left|\frac{d}{du}f_s(L(u))\right|
\le C_K e^{-\sigma L}
\]

for large `L`. Since exact and reference log-cross-ratios differ by only `O(p_m^-2)`, the segment joining them changes `L` by `O(p_m^-2)`. Therefore

\[
\boxed{
|f_s(L^E_{m,n})-f_s(L^0_{m,n})|
\le
C_K p_m^{-2}\min(1,e^{-\sigma L^0_{m,n}}).
}
\]

Now put

\[
q=2\sigma.
\]

The exact identity

\[
e^{-L/2}=(\sqrt{1+\chi}-\sqrt\chi)^2
\le\frac1{4\chi}
\]

implies

\[
e^{-\sigma L}\le C_\sigma\chi^{-q}.
\]

Thus long blocks contribute at worst

\[
p_m^{-2}(\chi^0_{m,n})^{-q}.
\]

## 4. Far blocks reduce to a gap-weighted prime tail

Assume

\[
p_n\ge2p_m.
\]

Then `Y=p_n-p_m >= p_n/2`, and

\[
\chi^0_{m,n}
=\frac{Y(X+Y+Z)}{XZ}
\ge\frac{Y^2}{XZ}.
\]

Hence

\[
(\chi^0_{m,n})^{-q}
\le
C_q X^q\left(\frac{g_n}{p_n^2}\right)^q,
\]

where `Z=g_n=p_{n+1}-p_n`.

For a dyadic prime block `P <= p_n < 2P`, Bertrand gives `g_n=O(P)` and telescoping gives

\[
\sum_{P\le p_n<2P}g_n=O(P).
\]

If `0<q<=1`, concavity yields

\[
\sum_{P\le p_n<2P}g_n^q
\le
N_P^{1-q}
\left(\sum g_n\right)^q
=O(P),
\]

where the crude bound `N_P=O(P)` is already sufficient. Consequently

\[
\sum_{P\le p_n<2P}
\left(\frac{g_n}{p_n^2}\right)^q
=O(P^{1-2q}).
\]

This dyadic tail converges exactly when

\[
q>\frac12.
\]

For `q>=1`, use

\[
g_n^q\le C P^{q-1}g_n
\]

to obtain the stronger dyadic bound `O(P^{-q})`.

Therefore for `q in (1/2,1)` the entire far tail for fixed `m` is

\[
O(X^q p_m^{1-2q}),
\]

and after multiplication by `p_m^-2` the outer sum is bounded by

\[
\sum_m X^q p_m^{-1-2q}.
\]

Since Bertrand gives `X=O(p_m)`, this is dominated by

\[
\sum_p p^{-1-q}<\infty.
\]

For `q>=1` the outer sum is even easier and is dominated by `sum p^-2`.

Thus the far-block double sum converges for

\[
\boxed{q>1/2,\quad\text{i.e.}\quad\sigma>1/4.}
\]

## 5. Near blocks are summable and do not set the threshold

For

\[
p_m<p_n<2p_m
\]

we discard the exponential gain and use only

\[
|f_s(L^E)-f_s(L^0)|\le C_Kp_m^{-2}.
\]

Chebyshev's prime-counting upper bound gives

\[
\#\{p_n<2p_m\}=O\left(\frac{p_m}{\log p_m}\right).
\]

Hence the near contribution is bounded by

\[
\sum_m\frac1{p_m\log p_m}.
\]

This converges. For example, on `2^k <= p < 2^{k+1}`, Chebyshev gives `O(2^k/k)` primes, while every summand is `O(1/(2^k k))`, so the dyadic block is `O(k^-2)`.

Therefore the near sector contributes no additional abscissa.

Combining the near and far estimates proves local uniform absolute convergence of the logarithmic product on every compact subset of

\[
\boxed{\operatorname{Re}s>1/4.}
\]

The resulting relative Euler product is holomorphic and nowhere zero there.

## 6. The boundary `Re s=1/4` really diverges

Fix one left frame `a<b`, equivalently fix `m`, and let `n -> infinity`.

The divided-difference identity gives

\[
\frac{\chi^E_{m,n}}{\chi^0_{m,n}}
=
\frac{D_V(b,c)D_V(a,d)}
     {D_V(a,b)D_V(c,d)}.
\]

Since

\[
V(x)=x+O(x^{-1}),
\]

we have

\[
D_V(b,c)\to1,
\qquad
D_V(a,d)\to1,
\qquad
D_V(c,d)\to1.
\]

But

\[
D_V(a,b)>1
\]

because `V'(x)>1` for finite `x>2`. Therefore

\[
\boxed{
\delta u_{m,n}\to-\eta_m,
\qquad
\eta_m:=\log D_V(a,b)>0.
}
\]

Also `chi^0_{m,n}->infinity`, so

\[
L^E_{m,n}-L^0_{m,n}\to-2\eta_m<0.
\]

For real `s>0`, it follows that the relative logarithmic factor is eventually negative and satisfies

\[
|f_s(L^E_{m,n})-f_s(L^0_{m,n})|
\asymp_m e^{-sL^0_{m,n}}.
\]

At `s=1/4`,

\[
e^{-L/4}
=\frac1{\sqrt{1+\chi}+\sqrt\chi}
\asymp\chi^{-1/2}.
\]

For fixed `X=b-a`, Bertrand gives `d=p_{n+1}<2p_n`; hence

\[
\chi^0_{m,n}
=\frac{Y(X+Y+Z)}{XZ}
\le C_m\frac{p_n^2}{g_n}.
\]

Therefore

\[
e^{-L^0_{m,n}/4}
\ge c_m\frac{\sqrt{g_n}}{p_n}
\ge c'_m\frac1{p_n}.
\]

Euler's divergence

\[
\sum_p\frac1p=\infty
\]

now gives

\[
\boxed{
\sum_n
|f_{1/4}(L^E_{m,n})-f_{1/4}(L^0_{m,n})|
=\infty.
}
\]

Because the real terms are eventually all negative, the fixed-`m` relative subproduct itself tends to zero at `s=1/4` rather than merely failing absolute convergence.

The same estimate gives failure of absolute convergence whenever `0<Re s<=1/4`.

Thus `1/4` is the exact abscissa of absolute convergence for this canonical all-block relative Ruelle sector.

## 7. Relation to the distinguished cuffs

For a long block, the cross-ratio has the asymptotic shape

\[
\chi_{m,n}
\asymp
\frac{(p_n-p_m)^2}{X_m Z_n}.
\]

Hence

\[
\boxed{
e^{-L_{m,n}/4}
\asymp
\frac{\sqrt{X_mZ_n}}{p_n-p_m}.
}
\]

The end spacings are precisely the local quantities encoded by the distinguished cuff lengths:

\[
X_m\asymp4p_m e^{-\ell_{L,m}/2},
\qquad
Z_n\asymp4p_n e^{-\ell_{R,n}/2}.
\]

Thus the boundary weight is, up to the slowly varying endpoint scale,

\[
e^{-L_{m,n}/4}
\asymp
\frac{4\sqrt{p_mp_n}}{p_n-p_m}
\exp\left[-\frac{\ell_{L,m}+\ell_{R,n}}4\right].
\]

This is qualitatively different from the local tangent results, which retain ratios or differences of neighboring cuffs. The all-block relative sector couples **two distant cuff scales through the span of the block**. The quarter-plane threshold occurs when the square-root end-gap weight becomes just large enough that summing over the far prime endpoint contains the divergent prime harmonic series.

No arithmetic weight was chosen to force this: the square root is imposed by the exact hyperbolic relation `L=4 asinh sqrt(chi)` and the value `s=1/4`.

## 8. Why this is not a hidden modular/RH restatement

The number `1/4` also appears in modular scattering after the change of variables in `zeta(2s)`, but that is not the mechanism here. PF-044 already showed that the modular `Gamma(2)` zeta factor is universal and gap-blind, while PF-055/PF-071 rule out a global arithmetic-Fuchsian explanation for the gap-sensitive sector.

Here `1/4` is an **abscissa of a relative geometric Euler product**, not a line on which zeros have been proved or conjectured to lie. The product is zero-free throughout its domain of convergence `Re s>1/4`.

Any connection to RH would require a canonical continuation across this abscissa and a new spectral interpretation of its divisor. Neither is presently established.

## 9. Prior-art / novelty audit

Known theory provides:

- ordinary Selberg/Ruelle Euler products for compact, cofinite, convex-cocompact, and suitable geometrically finite hyperbolic systems;
- relative Laplacian determinants when resolvent/heat differences satisfy trace-class hypotheses (Muller-type relative determinant theory, Borthwick--Judge--Perry, Aldana and related work);
- extensive rigidity theory for simple length spectra, including infinite-type surfaces;
- thermodynamic formalism for countable-state systems under hypotheses very different from the prime-flute's positive-length primitive accumulation.

Those results do not supply this product. In particular, Borthwick--Judge--Perry treat surfaces hyperbolic near infinity under controlled perturbations, while Aldana treats finite-area cusp surfaces under controlled conformal changes; the present pair is infinite type with infinitely many cusps and non-discrete primitive length spectrum.

Directed searches for `relative Ruelle zeta`, `relative Selberg zeta length spectrum ratio`, `simple geodesic zeta`, and countable/infinite-type Fuchsian relative dynamical zetas did not locate the construction

\[
\boxed{
V(p_n)=\pi\cot(\pi/p_n)
\quad/\quad
V_0(p_n)=p_n
\quad+\quad
\text{all finite consecutive-block separators}
}
\]

or the exact `1/4` abscissa above.

Novelty is **not** claimed for cross-ratios, Ruelle factors, prime harmonic divergence, or relative determinant theory separately. The narrow candidate is the geometrically forced reference pair plus the canonical all-block orbit family and its exact convergence threshold.

## 10. Research consequence

PF-083 showed that purely local exact/reference corrections are too summable to create a divisor. PF-084 shows that **nonlocal proliferation changes the analytic class**: summing the same tiny projective defect over every finite consecutive block creates a genuine natural boundary of ordinary Euler-product convergence at `Re s=1/4`.

This is the first global relative-zeta candidate in the program whose convergence domain is generated by an interaction between exact prime-circle geometry and nonlocal prime-flute topology rather than by selecting a classical Dirichlet series.

The decisive next test is not to invent a continuation. It is to ask whether `R_rel^block` is the Fredholm/relative determinant of a canonically defined operator, or whether the `1/4` abscissa is only a property of this selected simple-block sector. Failure of any intrinsic operator realization would demote the construction to an interesting geometric Euler product rather than a spectral mechanism.

## Lean / symbolic candidates

1. Formalize the four-point exact/reference divided-difference identity for the cross-ratio.
2. Prove `|log(chiE/chi0)| <= C/p_m^2` from a uniform bound on `log V'`.
3. Formalize `e^{-L/2}=(sqrt(1+chi)-sqrt(chi))^2 <= 1/(4chi)` for `L=4 asinh sqrt chi`.
4. Formalize the dyadic gap inequality `sum g_i^q <= N^(1-q)(sum g_i)^q` for `0<q<=1`.
5. Formalize the fixed-left-end limit `chiE/chi0 -> 1/D_V(a,b)` and the resulting boundary divergence after importing `sum_p 1/p = infinity`.
