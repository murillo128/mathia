# PC-021 — regular linear probes of primitive shells are Möbius-tautological before spectralization

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for regular fixed linear ambient probes followed by ordinary Dirichlet scale transforms. The underlying divisor/Möbius identities are classical; no novelty is claimed for them.

## 1. Claim

PC-015 showed two apparently different collapses: the full interior cyclotomic field acquires an explicit `1/zeta(s)` under the ordinary Dirichlet transform, while the fixed round-sphere linear spectral package reduces to Ramanujan sums. Both are instances of a stronger measure-level statement.

Let

\[
R_n:=\sum_{\zeta^n=1}\delta_\zeta
\]

be the counting measure of **all** vertices of the regular `n`-gon and

\[
P_n:=\sum_{\operatorname{ord}(\zeta)=n}\delta_\zeta
\]

be the counting measure of the primitive/new-vertex shell. Then the birth decomposition is exactly

\[
\boxed{R_n=\sum_{d\mid n}P_d,}
\]

so Möbius inversion gives the measure identity

\[
\boxed{P_n=\sum_{d\mid n}\mu(n/d)R_d.}
\]

Therefore the reciprocal-zeta factor is already present **before choosing any regular linear geometric or spectral observable**.

## 2. Measure-valued Dirichlet identity

Work in the Banach space `M(S^1)` of finite complex Borel measures with total-variation norm. Since

\[
\|P_n\|=\varphi(n),\qquad \|R_n\|=n,
\]

both series below converge absolutely in `M(S^1)` for `Re(s)>2`. Summing the Möbius inversion formula and writing `n=dk` yields

\[
\begin{aligned}
\sum_{n\ge1}\frac{P_n}{n^s}
&=\sum_{d\ge1}\frac{R_d}{d^s}
  \sum_{k\ge1}\frac{\mu(k)}{k^s}\\
&=\boxed{\frac1{\zeta(s)}\sum_{d\ge1}\frac{R_d}{d^s}}.
\end{aligned}
\]

Thus `1/zeta(s)` is not produced by a later PDE, Green function, Fourier decomposition, or spectral diagonalization. It is the Dirichlet-series image of the exact statement that every polygon decomposes into primitive birth shells.

The half-plane `Re(s)>2` is only the convenient Banach-valued absolute-convergence region. Particular scalar observables can converge further left, but any continuation obtained from the right-hand side still inherits the same Möbius factorization unless an operation falls outside the hypotheses below.

## 3. Universal consequence for regular fixed linear probes

Let `X` be a Banach space and let

\[
L:M(S^1)\to X
\]

be any **fixed bounded linear map**. Applying `L` to the measure-valued identity gives, for `Re(s)>2`,

\[
\boxed{
\sum_{n\ge1}\frac{L(P_n)}{n^s}
=\frac1{\zeta(s)}
 \sum_{d\ge1}\frac{L(R_d)}{d^s}.
}
\]

This covers, for example, integration against a fixed continuous test kernel, Fourier coefficients, Poisson/harmonic extension on any compact subdisk separated from the boundary charges, and any other regular ambient linear filter that is continuous on finite measures in the chosen target norm.

Hence a proposed chain of the form

\[
\boxed{
\text{primitive shell}
\to\text{fixed regular linear ambient operator}
\to\text{ordinary Dirichlet transform in }n
}
\]

cannot provide an independent zeta-zero mechanism. Any reciprocal-zeta singularity is algebraically upstream of the spectral interpretation.

This strictly generalizes the rotationally invariant round-sphere obstruction of the spherical PC-015: rotational invariance is not needed for the scale-factorization theorem. It also explains the analytic full-field PC-015 as one regularized realization of the same primitive-versus-full decomposition.

## 4. Fourier shadow: Ramanujan sums are one matrix element

For the test function `f_k(z)=z^k`,

\[
\int_{S^1}z^k\,dP_n(z)=c_n(k),
\]

the Ramanujan sum. For the full polygon,

\[
\int_{S^1}z^k\,dR_d(z)
=\begin{cases}
d,&d\mid k,\\0,&d\nmid k.
\end{cases}
\]

Therefore the measure theorem immediately gives the classical identity

\[
\boxed{
\sum_{n\ge1}\frac{c_n(k)}{n^s}
=\frac{\sigma_{1-s}(k)}{\zeta(s)}.
}
\]

So the Ramanujan-sum collapse is not a special accident of Fourier analysis. Fourier modes simply expose one scalar coordinate of the more basic measure-valued Möbius inversion.

## 5. Independent multilinear shell indices factor as well

The obstruction extends to bounded multilinear observables **when the shell indices are independently transformed**. For a bounded bilinear map

\[
B:M(S^1)\times M(S^1)\to X,
\]

absolute convergence for `Re(s),Re(t)>2` gives

\[
\boxed{
\sum_{m,n\ge1}\frac{B(P_m,P_n)}{m^s n^t}
=\frac1{\zeta(s)\zeta(t)}
 \sum_{a,b\ge1}\frac{B(R_a,R_b)}{a^s b^t}.
}
\]

Likewise a bounded `r`-linear observable with `r` independently Dirichlet-transformed shell indices acquires one reciprocal-zeta factor per index.

This rules out a broader class of apparently nonlocal constructions in which several primitive shells are first coupled by a fixed regular multilinear kernel and then each level is diagonalized separately by an ordinary Dirichlet weight.

## 6. Crucial exception: the common vertex is a singular boundary probe

The theorem also identifies precisely why the anchored common-vertex observable of PC-001 is different.

Consider

\[
f(\zeta)=\log|1-\zeta|.
\]

This is singular at the common vertex `1`. Every full polygon measure `R_n` contains an atom at `1`, so

\[
\int f\,dR_n
\]

is not a finite regular linear observable at all. By contrast, for every `n>1` the primitive shell `P_n` excludes `1`, and

\[
\int f\,dP_n
=\log|\Phi_n(1)|
=\Lambda(n).
\]

Thus the anchor is not merely a marked point that breaks rotational symmetry. It is a **singular boundary observation point at which primitive-shell extraction removes a divergence present in every full layer**.

This is a mathematically precise escape hatch from the regular-linear no-go theorem. Its simplest scalar output is already classical,

\[
\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
=-\frac{\zeta'(s)}{\zeta(s)},
\]

so singularity alone is not enough. But any future linear anchored mechanism that genuinely escapes the universal `1/zeta` factorization must involve a canonically justified singular/renormalized boundary operation rather than a regular fixed kernel.

## 7. What is not ruled out

The theorem deliberately does **not** cover several live branches:

1. **same-index nonlinear or diagonal observables**, such as a renormalized `B(P_n,P_n)` followed by one scale transform; the shared index couples the divisor expansions and does not factor into two independent Dirichlet series;
2. **singular kernels or renormalized energies**, including logarithmic self/mutual energies, when the bilinear form is not bounded on all finite measures;
3. **shell-dependent operators or metrics** whose definition changes nonlinearly with `P_n`;
4. **nonseparable scale dynamics** that is not ordinary independent weighting by `n^{-s}`;
5. **global uniformization/accessory data** such as PC-016/PC-017, where the Poincaré metric, Fuchsian projective connection, monodromy, determinant, or Liouville action depends nonlinearly on the puncture configuration.

This boundary is important: the canonical nonlinear uniformization defect is not an ad hoc exception to the negative evidence. It lies exactly outside the linear Möbius-factorization class proved here.

## 8. Prior art / novelty audit

The mathematical identities underlying this finding are classical:

- `R_n=sum_{d|n}P_d` is the elementary decomposition of all `n`-th roots into primitive divisor shells;
- Möbius inversion gives the reverse formula;
- `sum mu(n)n^{-s}=1/zeta(s)` is classical;
- the Fourier specialization is the standard Ramanujan-sum Dirichlet series already anchored in `SOURCES.md`.

No novelty is claimed for any of those identities, nor for applying a bounded linear map to an absolutely convergent Banach-valued series.

The useful prime-circle contribution is the **scope classification**: all regular fixed linear ambient probes, and all fixed bounded multilinear probes with independently transformed shell indices, inherit reciprocal zeta directly from birth-shell Möbius inversion. They therefore cannot be counted as independent spectral explanations of the zeros.

## 9. Research consequence

After PC-015, PC-019, PC-020, and the present result, a credible continuation must retain the anchor while avoiding both purely local jets and regular linear ambient filtering. The cleanest surviving region is

\[
\boxed{
\text{anchored} + \text{nonlocal} + \text{nonlinear or singularly renormalized}.
}
\]

The existing cyclotomic uniformization defect of PC-017 is a canonical example of that class. Future work should prioritize its global accessory/monodromy, Liouville-action, Weil-Petersson, or other genuinely nonlinear endpoint data rather than searching for another fixed linear kernel whose scale transform can only reproduce Möbius inversion.