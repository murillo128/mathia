# PF-022 — distinguished-cuff Selberg half-threshold is renormalizable and non-spectral

**Status:** `NEGATIVE/OBSTRUCTION` + `EXACT-DERIVED` + `POSITIVE-RELATIVE-REGULARIZATION`. The original absolute half-threshold argument uses the previously recorded square-summability input for the logarithmic mesh; the exact-vs-linearized relative strengthening in Section 9 needs only the explicit endpoint map, elementary asymptotics, and Bertrand's postulate.

This note tests the most direct Selberg-type object built from the distinguished prime-flute cuffs themselves. The classical Selberg Euler factor is standard; the custom content is the exact specialization to the prime endpoint geometry and the resulting renormalization at `s=1/2`.

The conclusion is negative: the canonical cuff-only Euler subproduct does have an absolute-convergence threshold at `Re(s)=1/2`, but at the real boundary point its entire divergence is an explicitly removable endpoint-growth factor. After that geometric renormalization the product converges to a finite positive constant. Thus this occurrence of `1/2` cannot by itself encode Riemann-zero-type spectral information.

A later exact/reference audit strengthens this: comparing the true endpoint flute `cot(pi/p_n)` with its projective linear reference `p_n`, the distinguished-cuff length defects are in `ell^1`. Consequently both the relative cuff Ruelle product and the relative cuff Selberg product converge locally uniformly and are nowhere zero throughout `Re(s)>0`. The exact finite-scale correction therefore does not restore a critical divisor in this most direct cuff sector.

## 1. Exact cuff variable

Recall the exact prime-flute identities

```text
u_n = cot(pi/p_n)
h_n = log(u_n/u_{n-1}) > 0
q_n = exp(-ell_n/2) = tanh(h_n/4).
```

Also

```text
sum_{n=m}^N h_n = log(u_N/u_{m-1}).
```

The existing arithmetic audit records

```text
sum_n h_n^2 < infinity.
```

Hence `h_n -> 0`, and therefore

```text
q_n = h_n/4 + O(h_n^3).
```

Since the finite telescoping sum of the `h_n` tends to `+infinity`, while `sum h_n^3` converges, we obtain the useful ideal-class fingerprint

```text
sum_n q_n = infinity,
sum_n q_n^2 < infinity.
```

More generally, using `h_n = O(g_{n-1}/p_n)`, the Baker-Harman-Pintz bound `g_n << p_n^theta` with `theta<1`, and a dyadic estimate

```text
sum_{p_n in [x,2x]} g_n^alpha
    <= (max g_n)^(alpha-1) sum g_n
    << x^(theta(alpha-1)) x,
```

one gets

```text
sum_n q_n^alpha < infinity
```

for every fixed `alpha>1`.

Thus the sequence is in every `ell^alpha`, `alpha>1`, but not in `ell^1`.

## 2. The natural distinguished-cuff Selberg subproduct

For a primitive closed geodesic of length `ell`, the standard Selberg factor is

```text
prod_{k=0}^infinity (1 - exp(-(s+k) ell)).
```

Every distinguished pants cuff is a primitive closed geodesic. Therefore the marked prime-flute geometry canonically singles out the partial Euler product

```text
Z_cuff,m,N(s)
  = prod_{n=m}^N prod_{k=0}^infinity
      (1 - exp(-(s+k) ell_n))

  = prod_{n=m}^N prod_{k=0}^infinity
      (1 - q_n^(2(s+k))).
```

This is not asserted to be the Selberg zeta function of the full infinite surface. PF-006/PF-020 already show that the ordinary full Selberg product is obstructed by the separate family of primitive lengths accumulating at zero. `Z_cuff` is only the most natural candidate built directly from the distinguished cuff sequence.

Because `sum q_n^alpha < infinity` for every `alpha>1`, the double product converges absolutely for

```text
Re(s) > 1/2.
```

At the real point `s=1/2`, the `k=0` terms are `1-q_n` and `sum q_n=infinity`, while all `k>=1` terms are absolutely summable. Thus `1/2` is the exact real boundary for this direct Euler construction.

## 3. Exact renormalization at `s=1/2`

Set `x=h_n/4`. The elementary identity

```text
1 - tanh x = exp(-x) / cosh x
```

gives exactly

```text
1 - q_n
  = exp(-h_n/4) sech(h_n/4).
```

Multiplying from `m` to `N`,

```text
prod_{n=m}^N (1-q_n)
 = exp(-(1/4) sum_{n=m}^N h_n)
   prod_{n=m}^N sech(h_n/4)

 = (u_{m-1}/u_N)^(1/4)
   prod_{n=m}^N sech(h_n/4).
```

Since

```text
log sech x = -x^2/2 + O(x^4)
```

and `sum h_n^2<infinity`, the product

```text
prod_{n=m}^infinity sech(h_n/4)
```

converges to a strictly positive finite constant.

For the remaining Selberg factors at `s=1/2`,

```text
prod_{k=1}^infinity (1-q_n^(2k+1)),
```

absolute convergence follows from

```text
sum_n sum_{k>=1} q_n^(2k+1)
 = sum_n q_n^3/(1-q_n^2)
 < infinity.
```

Therefore there is a constant `C_m` with

```text
0 < C_m < infinity
```

such that

```text
u_N^(1/4) Z_cuff,m,N(1/2) -> C_m.
```

Equivalently, because `u_N ~ p_N/pi`,

```text
Z_cuff,m,N(1/2)
  ~ C'_m p_N^(-1/4)
```

with `0<C'_m<infinity`.

So the vanishing of the unrenormalized partial product at the half-threshold is exactly the coarse radial endpoint growth, plus a convergent positive local correction. There is no zero or sign/phase phenomenon left at the real boundary point after the natural geometric normalization.

## 4. What this rules out

The chain

```text
distinguished cuff lengths
    -> Selberg-type cuff Euler product
    -> threshold Re(s)=1/2
    -> Riemann critical-line mechanism
```

is not viable on the basis of the threshold itself.

The number `1/2` appears because

```text
q_n = exp(-ell_n/2)
```

sits at the `ell^1` / `ell^(1+epsilon)` boundary. At `s=1/2`, the first Selberg factor is exactly `1-q_n`; its divergent linear term is the telescoping logarithmic mesh `sum h_n`, and the non-telescoping remainder is absolutely summable.

Thus this is another instance of the PF-002 mechanism: a local scalar observable of one distinguished cuff loses the fine relational prime-gap information in its divergent part.

The finite positive renormalized constant still depends on the whole local cuff sequence, but treating that scalar as a new arithmetic invariant would merely repackage convergent prime-gap corrections. No independent Laplacian, resonance, scattering, or trace-formula mechanism selects it.

## 5. What is *not* ruled out by the absolute-product argument

The original half-threshold calculation alone does **not** prove conditional convergence or analytic continuation of the absolute cuff product on the vertical line

```text
s = 1/2 + it, t != 0.
```

At such points the leading term contains phases `q_n^(2it)`, and cancellation would depend on the distribution of the logarithmic gap variables. Without an independent spectral theorem selecting that continuation, studying those phases would amount to studying another Dirichlet series of prime-gap data, so it is not promoted as a candidate here.

Section 9 below is different: it compares the exact cuff sector with the geometrically forced projective reference and obtains an honest relative product on the whole open right half-plane. That does not analytically continue the *absolute* cuff product.

Nor does this note affect the genuinely relational multi-gap sector from PF-004/PF-019, where cross-ratios survive cusp normalization and enter actual cross-cusp scattering coefficients.

## 6. Operator-ideal observation

The exact size statement

```text
(q_n) in ell^2 but not ell^1
```

means that the purely diagonal bookkeeping operator `Q=diag(q_n)` would be Hilbert-Schmidt but not trace class. Hence a genus-one / Carleman-Fredholm regularization is the minimal standard determinant regularization for that artificial diagonal model.

This is **not** yet a spectral operator attached to the Laplacian and should not be promoted to a natural determinant without an independent gluing/scattering construction whose singular values are genuinely comparable to the `q_n`.

## 7. Literature / novelty check

The Selberg factor

```text
prod_[primitive gamma] prod_{k>=0}
  (1-exp(-(s+k) ell_gamma))
```

is classical. Existing continuation results located in the search concern compact, cofinite, convex-cocompact, or more generally geometrically finite Fuchsian groups; for example Borthwick-Judge-Perry study geometrically finite surfaces and relative determinants under controlled perturbations, and Fedosova-Pohl treat geometrically finite groups with non-expanding cusp monodromy under transfer-operator hypotheses. These results do not supply a standard Selberg determinant for this infinitely generated prime-flute with primitive lengths accumulating at zero.

The tight-flute literature located in the project (Arredondo-Morales-Ramirez and related work) treats the zero-twist geometry, first-kind criterion, and parabolicity, not this distinguished-cuff Euler subproduct.

The relative-product strengthening in Section 9 is also not an invocation of a general relative-Laplacian theorem: it is a direct locally uniform convergence argument for one canonically distinguished primitive-geodesic sector. Standard relative determinant theory explains why ratios are natural when two geometries are sufficiently close, but its hypotheses are not being asserted for the full exact/projective prime-flute pair.

Targeted searches did not locate either the exact prime-flute renormalization above or the exact-vs-linearized distinguished-cuff factor below. No general-theorem novelty is claimed: the useful project-specific conclusion is that the most direct cuff-based Selberg candidate produces a removable half-threshold, and even its canonical exact/projective relative completion is zero-free on `Re(s)>0`.

## 8. Geometry preserved

Everything here uses the exact interior hyperbolic cuff lengths coming from the orthogonal-circle construction. The ambient inversion/interior-exterior duality remains exactly as recorded in PF-017 but plays no role in this product, because it is not an internal symmetry of the prime-flute Laplacian.

The linearized comparison in Section 9 is not a featureless background: it is the projective reference obtained by replacing the exact endpoint map `pi*cot(pi/p)` by its asymptotic projective coordinate `p`. Thus it preserves the ordered prime labels and the same projective gap geometry while isolating the finite-scale cotangent defect, exactly as in PF-082/PF-083/PF-099.

## 9. Exact/projective cuff-length defect is `ell^1`

Let

\[
h_n^0=\log\frac{p_n}{p_{n-1}},
\qquad
h_n^E=\log\frac{\cot(\pi/p_n)}{\cot(\pi/p_{n-1})}.
\]

The irrelevant factor `pi` cancels in the ratio. Define the endpoint defect

\[
a(x)=\log\frac{\pi\cot(\pi/x)}{x}.
\]

Then there is an **exact coboundary identity**

\[
\boxed{
 h_n^E-h_n^0=a(p_n)-a(p_{n-1}).
}
\]

The elementary cotangent expansion gives

\[
a(x)
=-\frac{\pi^2}{3x^2}
-\frac{7\pi^4}{90x^4}
+O(x^{-6}),
\qquad
 a'(x)=\frac{2\pi^2}{3x^3}+O(x^{-5}).
\]

Thus `a` is eventually increasing to zero and, writing `g=p_n-p_{n-1}`,

\[
0<h_n^E-h_n^0
\le C\frac{g}{p_{n-1}^3}
\]

for all sufficiently large `n`. The signed mesh defect itself telescopes:

\[
\sum_{n=m}^{N}(h_n^E-h_n^0)
=a(p_N)-a(p_{m-1})
\longrightarrow -a(p_{m-1}).
\]

Now write the exact cuff-length function as

\[
\ell(h)=2\log\coth\frac h4,
\qquad
\ell'(h)=-\frac1{\sinh(h/2)}.
\]

Since `h_n^E>=h_n^0` eventually,

\[
|\ell_n^E-\ell_n^0|
\le
\frac{h_n^E-h_n^0}{\sinh(h_n^0/2)}
\le
2\frac{h_n^E-h_n^0}{h_n^0}.
\]

Also

\[
h_n^0
=\log\left(1+\frac{g}{p_{n-1}}\right)
\ge \frac{g}{p_n}.
\]

Therefore

\[
|\ell_n^E-\ell_n^0|
\le C\frac{p_n}{p_{n-1}^3}.
\]

Bertrand's postulate gives `p_n<2p_{n-1}`, hence

\[
\boxed{
|\ell_n^E-\ell_n^0|
=O(p_{n-1}^{-2}),
\qquad
\sum_n|\ell_n^E-\ell_n^0|<\infty.
}
\]

This statement is stronger than merely saying that each bare cuff has an `O(p^-2)` exact/reference correction: the whole distinguished-cuff deformation is absolutely summable in length coordinates. No prime-gap upper bound is needed; the gap cancels against the logarithmic mesh in the derivative of `ell(h)`.

Because `p_n/p_{n-1}->1`, both `h_n^0` and `h_n^E` tend to zero and therefore both cuff lengths tend to `+infinity`.

### Relative Ruelle cuff sector

Define

\[
\mathcal R_{\rm cuff,rel}(s)
=
\prod_n
\frac{1-e^{-s\ell_n^E}}
     {1-e^{-s\ell_n^0}}.
\]

Fix a compact `K` in `Re(s)>0`. For all sufficiently large `n`, every length between `ell_n^E` and `ell_n^0` is at least `1`, and

\[
\left|
\frac{\partial}{\partial L}
\log(1-e^{-sL})
\right|
=
\left|\frac{s}{e^{sL}-1}\right|
\le C_K.
\]

Hence

\[
\left|
\log\frac{1-e^{-s\ell_n^E}}
         {1-e^{-s\ell_n^0}}
\right|
\le C_K|\ell_n^E-\ell_n^0|.
\]

The `ell^1` estimate above gives locally uniform convergence of the logarithmic series. Therefore

\[
\boxed{
\mathcal R_{\rm cuff,rel}(s)
\text{ is holomorphic and nowhere zero on }\operatorname{Re}s>0.
}
\]

### Relative Selberg cuff sector

For one primitive length put

\[
Z_L(s)=\prod_{k=0}^{\infty}(1-e^{-(s+k)L}).
\]

For `L>=1` and `s` in a compact `K` of the open right half-plane,

\[
\left|
\frac{\partial}{\partial L}\log Z_L(s)
\right|
\le
\sum_{k=0}^{\infty}
\frac{|s+k|}{e^{(\operatorname{Re}s+k)L}-1}
\le C_K.
\]

Consequently

\[
\sum_n
\left|
\log\frac{Z_{\ell_n^E}(s)}{Z_{\ell_n^0}(s)}
\right|
\le
C_K\sum_n|\ell_n^E-\ell_n^0|<\infty
\]

apart from finitely many initial factors. Thus

\[
\boxed{
\mathcal Z_{\rm cuff,rel}(s)
:=
\prod_n
\frac{Z_{\ell_n^E}(s)}{Z_{\ell_n^0}(s)}
}
\]

also converges locally uniformly and is nowhere zero on `Re(s)>0`.

This is the distinguished-cuff analogue of PF-083's zero-free relative period-two sector, but its interpretation is sharper for PF-022: the absolute `1/2` threshold belongs to the shared projective background and disappears completely after the canonical exact/reference cancellation.

## 10. Updated boundary of the negative result

The strengthened obstruction is now

\[
\boxed{
\text{distinguished cuffs alone}
\;\not\Rightarrow\;
\text{a critical divisor, either absolutely or relatively against the projective reference}.
}
\]

The absolute product has a removable real half-threshold; the canonical relative exact/projective product has **no zeros anywhere in the open right half-plane**. This closes the possibility that the finite-scale `pi*cot(pi/p)` correction rescues the distinguished-cuff Euler sector after the projective background is divided out.

It still does **not** construct, continue, or rule out a full relative Selberg/Ruelle zeta of the infinite prime-flute. Nonlocal primitive words are a separate issue (PF-084), and relative Laplacian/scattering comparability requires operator-theoretic hypotheses not implied merely by `sum |ell_n^E-ell_n^0|<infinity`. In particular, no global trace-class or compact-resolvent perturbation claim is made here.
