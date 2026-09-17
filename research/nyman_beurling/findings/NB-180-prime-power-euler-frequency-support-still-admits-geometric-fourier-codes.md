# NB-180 — Prime-power Euler frequency support still admits geometric Fourier codes

**Date:** 2026-09-17  
**Status:** `DERIVED + MATCHED-CONTROL + SOURCE-FIDELITY-BOUNDARY + PRIME-POWER-EULER-SUPPORT + COORDINATEWISE-DUAL + DFT-CODE + NB-179-REFINEMENT`.

`NB-179` shows that unrestricted scalar capped-Poisson probes can turn a completely generic packing of Poisson-width dipoles into a maximal coordinatewise phase code. The immediate repair suggested by `NB-178` is to restrict the probes to a source-natural arithmetic frequency set, such as the Euler frequencies `log n` with `Lambda(n) != 0`.

That restriction is still not enough if every selected frequency may be renormalized independently to unit capped-Poisson dual norm. A single prime-power tower

\[
 p^m,\qquad m=1,2,\ldots,
\]

already supplies an exact arithmetic progression of Euler frequencies

\[
 m\log p.
\]

On an explicit sequence of Poisson widths, those frequencies form an exact discrete Fourier code on the same generic packed dipoles used in `NB-179`. The resulting response matrix has all singular values on the `sqrt(N)` scale, hence the `NB-178` coordinatewise certificate again gives linear approximate complexity.

The distinction from the real source is decisive. In `-zeta'/zeta`, the same prime-power channels carry amplitudes

\[
 (\log p)p^{-m(1+a)},
\]

which are exponentially small across the tower used by the code. Retaining those amplitudes collapses the nuclear response exponentially. Thus **Euler frequency support is not yet source fidelity**: a source-selective coordinatewise probe class must retain the Euler amplitudes, or charge explicitly for the acquisition/renormalization needed to erase them.

## Claim

Fix `B>0`. Choose a prime `p` so large that

\[
\log p>\frac{\pi}{B}.
\tag{1}
\]

For every sufficiently large even integer `N`, put

\[
a_N:=\frac{\pi}{N\log p},
\qquad
m_0:=\frac N2.
\tag{2}
\]

Since

\[
2Na_N=\frac{2\pi}{\log p}<2B,
\]

the `2N` points

\[
y_j:=-B+(j-1)a_N,
\qquad 1\le j\le2N,
\tag{3}
\]

lie in `[-B,B]` for all sufficiently large `N`. For any `q>0` and `X>0`, define the packed dipoles

\[
\nu_i
:=
qX\bigl(\delta_{y_{2i}}-\delta_{y_{2i-1}}\bigr),
\qquad 1\le i\le N.
\tag{4}
\]

Each dipole has exact capped transport

\[
\mathsf D_{a_N}(\nu_i)=qX.
\tag{5}
\]

For `0<=k<=N-1`, choose the **actual Euler frequency**

\[
\lambda_k
:=
(m_0+k)\log p
=
\log\bigl(p^{m_0+k}\bigr).
\tag{6}
\]

Because `Lambda(p^m)=log p`, every `lambda_k` belongs to the support of the Dirichlet series for `-zeta'/zeta`.

Define

\[
M_k:=\max\{2,a_N\lambda_k\},
\qquad
f_k(u):=\frac{e^{-i\lambda_k u}}{M_k},
\tag{7}
\]

and the scalar probe

\[
\ell_k(\sigma)
:=
\frac1q\int f_k(u)\,d\sigma(u).
\tag{8}
\]

Then every `ell_k` is individually capped-Poisson contractive:

\[
\boxed{
|\ell_k(\sigma)|
\le
\frac{\mathsf D_{a_N}(\sigma)}q.
}
\tag{9}
\]

Let `A` be the complex `N x N` response matrix

\[
A_{ik}:=\ell_k(\nu_i).
\tag{10}
\]

There is an absolute constant

\[
c_*:=\frac{2\sqrt2}{3\pi}>0
\tag{11}
\]

such that every singular value of `A` satisfies

\[
\boxed{
s_j(A)\ge c_*X\sqrt N,
\qquad 1\le j\le N.
}
\tag{12}
\]

In fact the singular values are known exactly up to their column amplitudes:

\[
s_{k+1}(A)
=
\sqrt N\,
\frac{2X\,|\sin(a_N\lambda_k/2)|}{M_k}.
\tag{13}
\]

Consequently, the coordinatewise certificate of `NB-178` gives, over the complexified probe space,

\[
\boxed{
\mathfrak L_{a_N,q,X}^{\mathrm{pack}}(\epsilon)
\ge
N(c_*X-\epsilon)_+^2.
}
\tag{14}
\]

If one insists on real scalar probes, replace each `f_k` by its real and imaginary parts. This gives `2N` real probes. The realified response still has all `N` nonzero singular values at least `c_*X sqrt(N)`, so the `NB-178` bound remains linear in `N` with only an absolute change of constants. Thus the phenomenon is not an artifact of complex notation.

Now retain the **actual Euler amplitudes** from `NB-176`. With

\[
c_{m,a_N}:=(\log p)p^{-m(1+a_N)}
\tag{15}
\]

and the order-one normalizer `Z_{a_N}`, use instead the prime-power coordinates

\[
g_k(u)
:=
\frac{c_{m_0+k,a_N}}{Z_{a_N}}
 e^{-i\lambda_k u}.
\tag{16}
\]

Let `A^Eul` be their response matrix on the same dipoles. Then

\[
\boxed{
\|A^{\mathrm{Eul}}\|_*
\ll_p
X\sqrt N\,
 p^{-N(1+a_N)/2}.
}
\tag{17}
\]

Thus the frequency-only, independently normalized code has nuclear size `asymp X N^(3/2)`, whereas the genuine Euler-weighted response on exactly the same prime-power frequencies is exponentially suppressed.

## Derivation

### 1. The packed dipoles fit inside the support window

From (1)--(2),

\[
(2N-1)a_N<2Na_N=\frac{2\pi}{\log p}<2B.
\]

Hence (3) remains inside `[-B,B]`. The two atoms in each dipole are separated by exactly one Poisson width `a_N`, so the capped cost between them is `1`; this gives (5).

Nothing arithmetic has entered yet. This is exactly the generic geometric packing mechanism isolated by `NB-179`.

### 2. A single normalized Euler character is capped-Poisson contractive

For `h=|u-v|`,

\[
|e^{-i\lambda_k u}-e^{-i\lambda_k v}|
\le
\min\{2,\lambda_k h\}.
\]

Since `M_k>=2` and `M_k>=a_N lambda_k`,

\[
|f_k(u)-f_k(v)|
\le1,
\qquad
|f_k(u)-f_k(v)|
\le\frac h{a_N}.
\]

Therefore

\[
|f_k(u)-f_k(v)|
\le
\min\left\{1,\frac{|u-v|}{a_N}\right\}.
\tag{18}
\]

Applying (18) to any Jordan coupling of a zero-mass signed measure gives (9), exactly as in the capped-transport dual argument of `NB-179`.

The crucial point is what has *not* been charged: each frequency has been independently divided by `M_k`, but its Euler coefficient `Lambda(n)n^(-1-a_N)` has been discarded.

### 3. The powers of one prime produce an exact DFT frequency grid

Let

\[
x_i:=\frac{y_{2i-1}+y_{2i}}2
\]

be the center of the `i`th dipole. Then

\[
x_i=x_1+2a_N(i-1).
\tag{19}
\]

The dipole response is

\[
A_{ik}
=
\frac{X}{M_k}
\left(
 e^{-i\lambda_k y_{2i}}
 -e^{-i\lambda_k y_{2i-1}}
\right)
\]

\[
=
-\frac{2iX}{M_k}
\sin\left(\frac{a_N\lambda_k}{2}\right)
 e^{-i\lambda_k x_i}.
\tag{20}
\]

Using (2) and (6),

\[
2a_N\lambda_k
=
\frac{2\pi(m_0+k)}N.
\tag{21}
\]

Hence

\[
e^{-i\lambda_k x_i}
=
 e^{-i\lambda_k x_1}
 e^{-2\pi i(i-1)m_0/N}
 e^{-2\pi i(i-1)k/N}.
\tag{22}
\]

The first factor in (22) is a column phase, the second is a row phase, and the third is the standard `N x N` discrete Fourier matrix. Therefore

\[
A=R F_N D,
\tag{23}
\]

where `R` is unitary diagonal, `F_N^*F_N=N I_N`, and `D` is diagonal with

\[
|D_{kk}|
=
\frac{2X}{M_k}
\left|
\sin\left(\frac{a_N\lambda_k}{2}
\right)
\right|.
\tag{24}
\]

This proves the exact singular-value formula (13).

### 4. All Fourier directions stay uniformly nondegenerate

Because `m_0=N/2`,

\[
a_N\lambda_k
=
\pi\left(\frac12+\frac{k}{N}\right)
\in
\left[\frac\pi2,\frac{3\pi}2\right).
\tag{25}
\]

Thus

\[
\left|
\sin\left(\frac{a_N\lambda_k}{2}
\right)
\right|
\ge
\frac{\sqrt2}{2},
\tag{26}
\]

while

\[
M_k
\le
\frac{3\pi}{2}.
\tag{27}
\]

Combining (24), (26), and (27) yields

\[
|D_{kk}|
\ge
\frac{2\sqrt2}{3\pi}X
=c_*X.
\]

Equations (12)--(14) follow.

This is stronger than merely observing that prime powers are Euler frequencies. The prime-power tower supplies the **exact arithmetic progression in frequency** needed by the packed geometry, so no prime-gap theorem, approximation argument, or nonharmonic Fourier stability theorem is required.

### 5. Restoring the Euler amplitudes destroys the code scale

For the same prime-power tower, the actual logarithmic-derivative coefficient is

\[
c_{m,a_N}
=(\log p)p^{-m(1+a_N)}.
\]

The weighted response matrix has the same Fourier factorization as (23), but its column amplitudes are now

\[
|D^{\mathrm{Eul}}_{kk}|
=
\frac{2X}{Z_{a_N}}
(\log p)
 p^{-(m_0+k)(1+a_N)}
\left|
\sin\left(\frac{a_N\lambda_k}{2}\right)
\right|.
\tag{28}
\]

`NB-177` records the uniform lower bound `Z_a >= (log 2)/2` for `0<a<=1`. Hence

\[
\sum_{k=0}^{N-1}|D^{\mathrm{Eul}}_{kk}|
\ll_p
X
p^{-m_0(1+a_N)}.
\tag{29}
\]

Since the singular values of `R F_N D^Eul` are `sqrt(N)|D^Eul_kk|`,

\[
\|A^{\mathrm{Eul}}\|_*
=
\sqrt N
\sum_{k=0}^{N-1}|D^{\mathrm{Eul}}_{kk}|
\ll_p
X\sqrt N
p^{-N(1+a_N)/2},
\]

which is (17).

Equivalently, turning the actual Euler coordinate

\[
\frac{c_{m,a}}{Z_a}e^{-im(\log p)u}
\]

into the independently normalized unit probe (7) requires the acquisition multiplier

\[
\frac{Z_a}{M_k c_{m,a}}
\asymp_p
p^{m(1+a)}
\tag{30}
\]

through this tower. The maximal phase code is therefore purchased by an exponentially growing renormalization of exponentially weak source channels.

## Stress test and exact boundary

### Frequency support alone fails the matched-control test

The construction uses only frequencies `log n` with `Lambda(n)!=0`; in fact it uses powers of one fixed prime. Therefore a proposed source-natural certificate of the form

> choose any Euler-supported frequency and normalize that scalar character independently to the capped-Poisson unit ball

cannot distinguish actual Nyman arithmetic from the generic dipole packing of `NB-179`.

The arithmetic label on the frequency does not stop the matched control from producing a full Fourier code.

### The theorem is exact on a sequence of Poisson widths

The exact DFT alignment uses

\[
a_N=\frac{\pi}{N\log p}.
\]

This finding does **not** claim exact alignment for an arbitrary externally prescribed width `a_T`. The sequence `a_N -> 0` is enough for the intended falsification: Euler-frequency membership by itself cannot be a universally source-selective structural invariant.

A stronger arbitrary-width statement would require either a stability theorem for slightly nonuniform Fourier grids or a different packing construction. Neither is needed for the present boundary claim.

### Proper prime powers are essential to this exact construction

The arithmetic progression comes from

\[
\log(p^m)=m\log p.
\]

Thus the exact argument does not show the same failure for a probe class artificially restricted to **distinct primes only**. Such a class would need a separate matched-control audit.

For the actual logarithmic derivative, however, prime powers are genuine source channels: `Lambda(p^m)=log p` for every `m>=1`. A class advertised as preserving the full Euler-frequency support cannot discard them merely to avoid this control.

### Independent normalization is the real loophole

The negative result does not contradict `NB-176` or `NB-177`. Those findings retain the actual Euler amplitudes inside one source budget. Equation (17) shows precisely why that budget behaves differently.

What fails here is the intermediate idea that **frequency location plus coordinatewise metric normalization** might already be source-specific. It is not. The same frequency locations become maximally expressive once their amplitudes are individually renormalized away.

## Representation audit

The DFT factorization, the elementary contraction estimate for an exponential, and the prime-power support identity `Lambda(p^m)=log p` are generic/classical facts. The result should therefore not be represented as a new theorem about zeta, RH, or Nyman closure.

The line-specific content is the matched-control comparison:

1. `NB-178` says a dense coordinatewise response can certify large approximate source complexity.
2. `NB-179` says arbitrary scalar capped-Lipschitz probes can fake such a response geometrically.
3. `NB-180` sharpens that falsifier: even restricting the scalar probes to **genuine Euler prime-power frequencies** still permits the same geometric code if each channel is normalized independently.
4. The actual Euler amplitudes suppress exactly that control exponentially, identifying amplitude/acquisition budget rather than frequency membership as the next source-fidelity gate.

So the finding is a `MATCHED-CONTROL + SOURCE-FIDELITY-BOUNDARY`, not evidence that the true Nyman family has large source complexity.

## Prior-art assessment

A targeted search around Nyman--Beurling, prime-power Fourier frequencies, Dirichlet polynomials, and the logarithmic derivative found the expected classical ingredients: the expansion

\[
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{p}\sum_{m\ge1}
\frac{\log p}{p^{ms}},
\qquad \Re s>1,
\]

and standard Fourier/explicit-formula uses of prime-power frequencies. The discrete Fourier orthogonality used in (23) is elementary. I did not find a prior source combining these ingredients into the present capped-Poisson matched-control statement or the source-acquisition comparison (17)/(30).

No new external theorem is load-bearing: the prime-power expansion and the Euler amplitudes are already part of the line-local framework in `NB-176`, while the rest is an exact finite calculation. Therefore `SOURCES.md` does not need a new durable anchor for this finding.

## Consequences for the live frontier

`NB-179` left open whether a uniformly source-natural arithmetic probe class could rescue the coordinatewise certificate. `NB-180` removes one tempting but insufficient version of that idea:

\[
\boxed{
\text{Euler-frequency support}
+
\text{independent unit normalization}
\not\Rightarrow
\text{source selectivity}.
}
\]

The next useful probe class must keep at least one resource that the packed control cannot obtain for free. The most direct candidate is an **acquisition budget tied to the actual Euler channel strength**. In concrete terms, independently amplifying the `n`th channel should cost according to the inverse of `Lambda(n)n^{-1-a}` (with the capped-Lipschitz normalization included), rather than being granted at unit cost.

A successful source-specific certificate would then need to show spectral spread after paying that common acquisition budget, or prove that the actual Nyman template family couples coherently to many channels without the exponential renormalization exposed in (30). Merely replacing arbitrary Lipschitz probes by arithmetic frequency labels is no longer a discriminating move.
