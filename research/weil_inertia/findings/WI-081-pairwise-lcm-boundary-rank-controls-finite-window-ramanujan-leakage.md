# WI-081 — pairwise LCM boundary rank controls finite-window Ramanujan leakage

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + DECISIVE-NEGATIVE`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the finite-section escape left by WI-080 and now also identifies a substantial sharpness barrier for the pairwise-rank route.

For every pair of distinct scalar moduli `m,n`, finite-window interaction between their Ramanujan blocks is confined to a rank determined by the distance from the window length to the nearest multiple of their pairwise lcm. More precisely, with

\[
U_m^{(N)}=(e(ax/m))_{0\le x<N,\ a\in(\mathbf Z/m\mathbf Z)^\times},
\qquad
B_m^{(N)}=U_m^{(N)}(U_m^{(N)})^*,
\]

so that

\[
(B_m^{(N)})_{x,y}=c_m(x-y),
\]

put

\[
\ell_{m,n}=\operatorname{lcm}(m,n),
\qquad
r_{m,n}=N\bmod \ell_{m,n},
\]

and

\[
\boxed{
\delta_N(m,n)
:=
\min\{r_{m,n},\ \ell_{m,n}-r_{m,n}\}
}
\]

with `delta_N(m,n)=0` when `r_{m,n}=0`. Then

\[
\boxed{
\operatorname{rank}
\bigl((U_m^{(N)})^*U_n^{(N)}\bigr)
\le \delta_N(m,n).
}
\tag{1}
\]

The new sharpness statement is:

\[
\boxed{
\delta_N(m,n)\le \min\{\varphi(m),\varphi(n)\}
\quad\Longrightarrow\quad
\operatorname{rank}
\bigl((U_m^{(N)})^*U_n^{(N)}\bigr)
=\delta_N(m,n).
}
\tag{2}
\]

Thus the boundary-rank estimate is not merely an upper bound near a complete pairwise period: in that entire small-defect regime it is exact.

For distinct odd primes `p<q` there is a stronger global statement. Write

\[
\delta:=\delta_N(p,q),
\qquad
\delta=kq+s,
\qquad 0\le s<q.
\]

Because `delta<=pq/2`, if

\[
\boxed{s\ge p\quad\text{or}\quad q-s\ge p,}
\tag{3}
\]

then

\[
\boxed{
\operatorname{rank}
\bigl((U_p^{(N)})^*U_q^{(N)}\bigr)
=
\min\{\delta,p-1\}.
}
\tag{4}
\]

Consequently, when `q>=2p`, condition (3) fails only in the already-covered range `delta<p`, and one obtains for **every** `N`

\[
\boxed{
\operatorname{rank}
\bigl((U_p^{(N)})^*U_q^{(N)}\bigr)
=
\min\{\delta_N(p,q),p-1\}.
}
\tag{5}
\]

So for prime blocks separated by a factor at least two, finite-window leakage has the maximal rank permitted by the smaller Ramanujan space as soon as the boundary defect reaches `p-1`. There is no hidden pairwise-rank saving to extract there.

The close-prime exceptional strip is genuine rather than proof slack. For

\[
(p,q,\delta)=(11,13,47),
\]

one has

\[
\boxed{
\operatorname{rank}
\bigl((U_{11}^{(N)})^*U_{13}^{(N)}\bigr)=8<10=p-1
}
\tag{6}
\]

whenever `delta_N(11,13)=47`. Thus a universal formula `rank=min(delta,p-1,q-1)` is false; additional rank deficiency can occur only in the close-prime phase geometry not covered by (3).

## 1. Exact pairwise boundary factorization

Fix distinct `m,n` and write `ell=lcm(m,n)`. For primitive residues `a mod m` and `b mod n`, the fractions `a/m` and `b/n` are distinct modulo one: equality would identify two reduced fractions and force `m=n`. Therefore

\[
z_{a,b}:=e(b/n-a/m)
\]

is a nontrivial `ell`-th root of unity, so

\[
\sum_{x=0}^{\ell-1}z_{a,b}^x=0.
\tag{7}
\]

Write `N=q_0 ell+r`, `0<=r<ell`. The `(a,b)` entry of the cross Gram is

\[
\sum_{x=0}^{N-1}z_{a,b}^x
=
\sum_{x=0}^{r-1}z_{a,b}^x,
\tag{8}
\]

because the `q_0` complete periods vanish by (7). At matrix level, (8) writes the whole cross Gram as a product through the `r` retained sample coordinates, hence its rank is at most `r`.

But (7) also gives

\[
\sum_{x=0}^{r-1}z_{a,b}^x
=-\sum_{x=r}^{\ell-1}z_{a,b}^x,
\tag{9}
\]

which factors through the complementary `ell-r` coordinates. Therefore

\[
\operatorname{rank}((U_m^{(N)})^*U_n^{(N)})
\le \min\{r,\ell-r\}=\delta_N(m,n),
\]

proving (1). A translated consecutive source interval changes the two truncated Fourier systems only by diagonal unitary phase factors, so the rank depends on the window length and not its origin.

This is the pairwise finite-section version of the complete-period orthogonality in WI-080: all cross-modulus coupling is created by the coordinates that remain after cancelling complete pairwise periods.

## 2. The small-boundary rank bound is exact

Take the shorter representation in (8) or (9), of length

\[
\delta=\delta_N(m,n).
\]

Up to an overall sign and diagonal unitary phase factors, the cross Gram can be written

\[
G_{m,n}^{(N)}
=
(V_m^{(\delta)})^*V_n^{(\delta)},
\tag{10}
\]

where `V_m^(delta)` is the `delta x phi(m)` matrix obtained by sampling the distinct primitive `m`-th roots on `delta` consecutive coordinates, and similarly for `n`.

If

\[
\delta\le\min\{\varphi(m),\varphi(n)\},
\]

then both matrices have full row rank `delta` by the ordinary Vandermonde determinant argument. Equivalently,

\[
V_n^{(\delta)}:\mathbf C^{\varphi(n)}\to\mathbf C^\delta
\]

is surjective and

\[
(V_m^{(\delta)})^*:\mathbf C^\delta\to\mathbf C^{\varphi(m)}
\]

is injective. Their composition therefore has rank exactly `delta`, proving (2).

This closes one tempting refinement route. In the small-boundary regime no stronger algebraic estimate of the same pairwise cross-Gram rank can improve WI-081: the current upper bound is attained identically. Any gain there must use information not present in rank alone, such as coefficient magnitudes, singular values, dependencies across several modulus pairs, or a source representation richer than the scalar Ramanujan blocks.

## 3. Prime blocks are maximally mixed outside a narrow close-prime strip

Now let `p<q` be distinct odd primes. Since the complete cross period is `pq`, reduce as above to a nearest-boundary block of length

\[
0\le\delta\le pq/2.
\]

The range `delta<=p-1` is already settled by (2), because

\[
\varphi(p)=p-1,
\qquad
\varphi(q)=q-1.
\]

Assume henceforth `delta>=p` and write

\[
\delta=kq+s,
\qquad 0\le s<q.
\tag{11}
\]

A vector in the row kernel on the `p`-frequency side can be represented, after the `p`-point discrete Fourier transform, by a `p`-periodic sequence

\[
f=(f_0,\ldots,f_{p-1}),
\qquad
\sum_{r\bmod p}f_r=0.
\tag{12}
\]

Orthogonality to every nonzero `q`-frequency is equivalent to the `q` residue-class sums

\[
S_j
:=
\sum_{\substack{0\le t<\delta\\t\equiv j\; (q)}}f_{t\bmod p}
\qquad (j\bmod q)
\tag{13}
\]

being all equal: the nontrivial `q`-Fourier coefficients of the vector `(S_j)` must vanish.

From (11), the first `s` residue classes contain `k+1` samples and the remaining `q-s` classes contain `k` samples:

\[
S_j=\sum_{\ell=0}^{k}f_{j+\ell q}
\quad(0\le j<s),
\tag{14}
\]

\[
S_j=\sum_{\ell=0}^{k-1}f_{j+\ell q}
\quad(s\le j<q).
\tag{15}
\]

All subscripts of `f` are taken modulo `p`. Because `delta<=pq/2` and `p` is odd,

\[
k+1<p,
\qquad
k<p.
\tag{16}
\]

If `s>=p`, then `p` consecutive indices in the first region of (14) realize every residue modulo `p`, so the function

\[
H(j)=\sum_{\ell=0}^{k}f_{j+\ell q}
\]

is constant for a complete set of residues `j mod p`. Hence

\[
0=H(j+q)-H(j)=f_{j+(k+1)q}-f_j.
\tag{17}
\]

The shift `(k+1)q` is nonzero modulo `p` by (16), and since `p` is prime it generates `Z/pZ`. Thus `f` is constant. The zero-mean condition (12) forces `f=0`.

If instead `q-s>=p`, the same argument applied to the second region of (15) gives

\[
f_{j+kq}=f_j.
\tag{18}
\]

Here `k>=1` because `delta>=p`, while `k<p` by (16), so again the shift is nonzero modulo `p` and `f=0`.

Therefore the row kernel is trivial whenever (3) holds, and the cross Gram has full `p-1` row rank. Together with the small-boundary case this proves (4).

The only possible prime-phase exception after `delta>=p` is therefore

\[
q-p<s<p.
\tag{19}
\]

Such an interval exists only when

\[
q<2p.
\tag{20}
\]

When `q>=2p`, one of `s>=p` or `q-s>=p` always holds, proving the all-window formula (5).

### Exact close-prime counterexample

Condition (19) cannot simply be removed. For `p=11`, `q=13`, `delta=47=3\cdot13+8`, one has

\[
13-11<8<11.
\]

There is a convenient rational certificate for the rank. Let `M` be the `13 x 11` integer incidence matrix

\[
M_{j,r}
:=
\#\{0\le t<47:t\equiv j\pmod{13},\ t\equiv r\pmod{11}\}.
\tag{21}
\]

On the zero-mean `11`-periodic space, use the basis

\[
e_i-e_{10},\qquad 0\le i<10,
\]

and quotient the output by constants using the rows

\[
e_j-e_{12},\qquad 0\le j<12.
\]

Let `T` be the resulting `12 x 10` integer matrix. The complex Fourier cross Gram has the same rank as `T`: the two Fourier transforms are invertible on the relevant zero-mean/nonconstant subspaces.

Two independent zero-mean vectors lie in its kernel:

\[
(-1,1,0,-1,1,0,0,0,-1,1,0),
\tag{22}
\]

\[
(-1,0,1,-1,0,1,0,0,-1,0,1).
\tag{23}
\]

Both satisfy `Mf=0`, so `rank T<=8`. Conversely, the upper-left `8 x 8` minor of `T` has determinant

\[
\boxed{3},
\tag{24}
\]

so `rank T>=8`. Hence the rank is exactly `8`, proving (6).

This counterexample kills the stronger conjecture that prime-pair finite sections always attain `min(delta,p-1,q-1)`. The correct structural statement is instead maximal mixing away from the narrow close-prime strip (19), with genuine additional dependencies possible inside it.

## 4. From cross-Gram rank to surviving subspace dimension

Let

\[
\mathcal S_m^{(N)}=\operatorname{ran}U_m^{(N)},
\qquad
d_m=\dim\mathcal S_m^{(N)}=\min\{N,\varphi(m)\}.
\]

The last equality is again the Vandermonde rank formula. The restriction of `(U_n^(N))^*` to `S_m^(N)` has kernel exactly

\[
\mathcal S_m^{(N)}\cap(\mathcal S_n^{(N)})^\perp.
\]

Since `U_m^(N)` surjects onto `S_m^(N)`, rank-nullity and (1) give

\[
\boxed{
\dim(\mathcal S_m^{(N)}\cap(\mathcal S_n^{(N)})^\perp)
\ge d_m-\delta_N(m,n),
}
\tag{25}
\]

and symmetrically with `m,n` exchanged.

The interpretation is stronger than an entrywise small-correlation statement: pairwise finite-section nonorthogonality is carried by at most `delta_N(m,n)` principal-angle directions. Section 2 shows that this number of potentially interacting directions is exactly realized whenever the boundary defect is no larger than both Ramanujan dimensions.

## 5. Two-block inertia survives only outside the coupled directions

For `B_m=U_mU_m^*`,

\[
\langle x,B_mx\rangle=\|U_m^*x\|_2^2>0
\qquad(x\in\mathcal S_m\setminus\{0\}).
\tag{26}
\]

Therefore, for `alpha,beta>0`,

\[
A=\alpha B_m^{(N)}-\beta B_n^{(N)}
\]

is positive definite on

\[
\mathcal S_m^{(N)}\cap(\mathcal S_n^{(N)})^\perp
\]

and negative definite on the symmetric subspace. Hence

\[
\boxed{
 n_+(A)\ge(d_m-\delta_N(m,n))_+,
\qquad
 n_-(A)\ge(d_n-\delta_N(m,n))_+.
}
\tag{27}
\]

For example, with `N=1000`, `m=31`, `n=32`, the pairwise lcm is `992`, so

\[
\delta_{1000}(31,32)=8.
\]

Since `phi(31)=30` and `phi(32)=16`, every

\[
\alpha B_{31}^{(1000)}-\beta B_{32}^{(1000)}
\]

has at least `22` positive and `8` negative eigenvalues. The `992` complete samples below the window cancel exactly; only eight boundary directions can couple.

The strengthened sharpness results also show the limitation of this inertia gate. For separated prime blocks `p<q`, `q>=2p`, once `delta_N(p,q)>=p-1`, the cross Gram has full smaller-side rank, so (27) cannot force any positive subspace supported purely on `S_p∩S_q^perp`. A better pairwise argument must use more than rank.

## 6. Many-modulus signed inertia gate

After aggregating repeated copies of the same scalar modulus, let

\[
A_\omega=\sum_m\omega_m B_m^{(N)},
\qquad
\mathcal P=\{m:\omega_m>0\},
\qquad
\mathcal M=\{m:\omega_m<0\}.
\]

Primitive fractions with distinct reduced denominators are distinct Fourier nodes, so concatenating all positive-side dictionaries gives

\[
D_+
=
\dim\sum_{m\in\mathcal P}\mathcal S_m^{(N)}
=
\min\!\left(N,\sum_{m\in\mathcal P}\varphi(m)\right),
\tag{28}
\]

and similarly

\[
D_-
=
\min\!\left(N,\sum_{n\in\mathcal M}\varphi(n)\right).
\tag{29}
\]

Define

\[
\Delta_N
:=
\sum_{m\in\mathcal P}\sum_{n\in\mathcal M}
\delta_N(m,n),
\qquad
R_N:=\min\{D_+,D_-,\Delta_N\}.
\tag{30}
\]

The positive-negative cross Gram is a block matrix, so subadditivity of rank gives

\[
\operatorname{rank}(U_+^*U_-)
\le
\sum_{m\in\mathcal P}\sum_{n\in\mathcal M}
\operatorname{rank}(U_m^*U_n)
\le\Delta_N.
\tag{31}
\]

Hence

\[
\boxed{
 n_+(A_\omega)\ge D_+-R_N,
\qquad
 n_-(A_\omega)\ge D_--R_N.
}
\tag{32}
\]

Thus a signed scalar mechanism cannot erase a macroscopic part of either sign-side spectral dimension unless the aggregate opposite-sign boundary-rank budget is itself macroscopic.

Equation (32) remains intentionally crude. It sums pairwise ranks and therefore ignores linear dependencies shared among several boundary couplings, and it ignores coefficient magnitudes. The sharp pairwise results in Sections 2--3 make the distinction important: a large `Delta_N` is often a genuine pairwise capacity for mixing rather than an artifact of a weak bound, but it still need not equal the rank of the full many-family cross operator.

## 7. Consequence for the WI-079/WI-080 signed scalar escape

WI-079 isolated the sign-sensitive scalar problem as the indefinite Ramanujan Toeplitz operator rather than an ordinary positive sparse-moduli large sieve. WI-080 then showed that complete common-period Ramanujan blocks are mutually orthogonal projectors, so all useful cross-modulus signed interaction is created by finite time-limiting.

The present result makes that finite-section escape substantially more rigid:

1. near any complete pairwise period, the boundary-rank budget is **exact** until one of the two Ramanujan dimensions saturates;
2. for prime pairs `p<q` with `q>=2p`, the interaction rank is exactly `min(delta_N(p,q),p-1)` for every window length;
3. additional pairwise rank deficiency is a genuinely arithmetic close-prime phenomenon rather than a generic finite-window effect, as the exact `(11,13,47)` example demonstrates.

Therefore the next scalar repair cannot rely on the hope that a sharper generic pairwise-rank estimate will make the WI-081 budget small. On a broad prime subfamily the current rank count is already maximal. A surviving mechanism must exploit one of the pieces that rank deliberately discards: weighted singular values, cancellation inside the signed operator, coherent dependencies across many modulus blocks, the special close-prime/composite phase geometry, or a richer labelled/two-dimensional source interface before scalar projection.

This remains a structural barrier for a **proposed scalar reduction**, not a proof of the whole Yang--Yang fourth-moment theorem or a no-go for labelled/two-modulus dispersion. Mathia has not established that the full post-local-main Yang covariance is exactly `A_omega`.

## 8. Prior art and novelty boundary

The harmonic-analysis ingredients are classical:

- Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6; arXiv:1803.02970. Lemma 1 gives the complete-common-period Ramanujan convolution orthogonality used in WI-080.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals**, *IEEE Transactions on Signal Processing* 62:16 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`, and **Part II: FIR Representations and Applications**, ibid. 4158--4172, DOI `10.1109/TSP.2014.2331624`. These establish the Ramanujan-subspace language and exact orthogonal decomposition when the relevant periods divide the finite signal length.
- Srikanth V. Tenneti and P. P. Vaidyanathan, **Nested Periodic Matrices and Dictionaries: New Signal Representations for Period Estimation**, *IEEE Transactions on Signal Processing* 63:14 (2015), 3736--3750, DOI `10.1109/TSP.2015.2434318`. The paper records the qualitative finite-length near-orthogonality of periodic/Ramanujan subspaces.
- Finite geometric sums, Vandermonde rank, finite Fourier inversion, rank-nullity, and inertia lower bounds from positive/negative definite subspaces are classical linear algebra.

A targeted audit of the Ramanujan-subspace/Farey-dictionary/finite-periodic-dictionary literature located the exact complete-period projector theory and qualitative finite-length approximate-orthogonality results, but did not locate the exact nearest-pairwise-period rank formula in the small-boundary regime, the prime maximal-mixing theorem (3)--(5), or the close-prime exact counterexample (6). **No priority claim is made.** The durable Mathia content is the application and sharpening of these elementary identities at the signed Ramanujan operator interface isolated by WI-079--WI-080.

## 9. Falsification and remaining gates

1. **Distinct reduced denominators.** The pairwise argument requires `m!=n` after duplicate scalar moduli have been aggregated. Equal moduli are one coefficient block, not cross-modulus leakage.
2. **Rank, not norm.** Equations (1)--(6) count coupled directions. They do not bound the nonzero singular values sharply and do not imply that a signed weighted operator has large norm.
3. **Prime theorem is not a composite theorem.** Equations (3)--(5) use prime cyclicity to turn a nonzero translation into a generator of `Z/pZ`. The Yang effective scalar support contains composite lcms as well as prime subfamilies, so the separated-prime result is a structural diagnostic, not a full source theorem.
4. **Close-prime exceptions are real.** The exact `(11,13,47)` witness refutes the stronger all-prime maximal-rank conjecture. Any future use of (5) must retain the hypothesis `q>=2p` or the explicit phase condition (3).
5. **Many-family rank can be much smaller than the sum of pairwise ranks.** `Delta_N` is only a union bound for block ranks. Shared boundary directions could lower the global cross rank even when most pairwise ranks are individually maximal.
6. **Weights are unused by the inertia gate.** A stronger theorem may exploit small or oscillating `omega_m`; Sections 2--3 only show that pairwise rank itself cannot provide such a saving in the stated regimes.
7. **Source-faithful scalar reduction remains unproved.** The result applies exactly once a Yang remainder has genuinely been reduced to the scalar signed Ramanujan form `sum_m omega_m B_m^(N)`. It must not be applied before that reduction is established.
8. **Numerical search is not evidence.** Finite exact-rational experiments were used only to stress-test conjectures and discover the close-prime witness. The persisted theorem uses the symbolic proofs above and the explicit determinant/kernel certificate for `(11,13,47)`.

## 10. Consequence for the research program

The pairwise boundary-rank route is now close to exhausted as a generic mechanism. Its strongest cheap hope was that finite time-limiting might couple far fewer Ramanujan directions than the naive remainder length suggests. Equation (2) proves the opposite near pairwise periods, while (5) proves maximal coupling for every window on a broad separated-prime family.

The sign-sensitive scalar route therefore survives only through information that WI-081's rank quotient discards: **weighted spectral leakage rather than rank leakage, genuinely many-family dependencies, exceptional close-prime/composite phase structure, or a source-faithful labelled operator before scalarization**. Any future scalar attack should test one of those interfaces directly rather than attempting another generic improvement of `delta_N(m,n)`.
