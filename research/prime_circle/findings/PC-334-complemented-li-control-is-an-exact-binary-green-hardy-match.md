# PC-334 — complemented Li control is an exact binary Green-Hardy match

**Status:** `EXACT-DERIVED` + `DECISIVE-MATCHED-CONTROL` + `PRIOR-ART-CLASSICALIZATION` for the finite-alphabet loophole left by PC-325 and the normalized Li-subtracted Green-Hardy branch of PC-330--PC-333.

PC-325 proves that the full Green/relative spectral branch is phase-gauge and therefore factors through source Fourier magnitudes/autocorrelations, but it deliberately leaves open the possibility that a restrictive binary or support-indicator class could remove the generic phase-retrieval ambiguity. PC-330--PC-333 then specialize the surviving magnitude-only question to the canonical binary prime source after subtraction of the smooth Li-grid profile.

That finite-alphabet loophole closes exactly for the source-normalized magnitude/autocorrelation observables of the present branch. The literal complement of any binary support has the same centered Fourier-power profile after the natural energy normalization. More strongly, the PC-330 Li-grid subtraction has a canonical complemented occupancy profile which is a genuine probability for all sufficiently large prime conductors and makes the complemented residual an exact scalar multiple of the original residual. Consequently every normalized Fourier band, dyadic Green-Hardy profile, cyclic short-interval variance, and source-normalized two-level Green/Hilbert operator considered in PC-330--PC-333 is identical for the prime support and its literal binary complement.

The complement identity itself is elementary and classical; no novelty is claimed for it. The line-local content is the exact matched-control consequence for the current Prime-Circle Green-Hardy normalization, including survival through the full Li-profile subtraction.

## 1. A literal binary complement has the same normalized centered power

Let `G=Z/qZ`, let `A\subset G` be a nonempty proper support of size `k`, and put

\[
B:=G\setminus A,
\qquad
m:=|B|=q-k.
\tag{1}
\]

Write the corresponding probability vectors and the uniform probability as

\[
p_A=\frac{1_A}{k},
\qquad
p_B=\frac{1_B}{m},
\qquad
u=\frac1q\mathbf 1.
\tag{2}
\]

Since `1_B=1-1_A`, one has the exact centered identity

\[
\boxed{
p_B-\nu
=-\frac{k}{m}(p_A-\nu).
}
\tag{3}
\]

For every nonzero Fourier mode `h`, therefore,

\[
\boxed{
\widehat p_B(h)
=-\frac{k}{m}\widehat p_A(h).
}
\tag{4}
\]

If

\[
\mu_A:=\|p_A-\nu\|_2^2,
\qquad
\mu_B:=\|p_B-\nu\|_2^2,
\tag{5}
\]

then

\[
\mu_B=\left(\frac{k}{m}\right)^2\mu_A.
\tag{6}
\]

Hence the complete normalized Fourier-power profile is identical:

\[
\boxed{
\frac{|\widehat p_B(h)|^2}{\mu_B}
=
\frac{|\widehat p_A(h)|^2}{\mu_A}
\qquad(h\ne0).
}
\tag{7}
\]

Up to the harmless common Fourier-normalization convention, (7) is equality of the complete centered diffraction/autocorrelation data after source-energy normalization. Unlike the continuous phase controls of PC-325, `B` is again a literal binary support.

## 2. Complementing an arbitrary smooth baseline

The same identity survives subtraction of a nonuniform probability baseline. Let `w` be any probability vector on `G` and set

\[
c:=\frac{k}{m}.
\tag{8}
\]

Define its complementary occupancy profile by

\[
\boxed{
w^{\mathrm c}
:=\nu-c(w-\nu)
=\frac{\mathbf 1-k w}{m}.
}
\tag{9}
\]

Its total mass is exactly one. Whenever `kw(x)\le1` pointwise, `w^c` is also nonnegative and is therefore a probability vector. The residuals

\[
d_A:=p_A-w,
\qquad
d_B^{\mathrm c}:=p_B-w^{\mathrm c}
\tag{10}
\]

then satisfy

\[
\boxed{
d_B^{\mathrm c}=-c\,d_A.
}
\tag{11}
\]

Thus for every frequency

\[
\widehat d_B^{\mathrm c}(h)
=-c\,\widehat d_A(h),
\qquad
\|d_B^{\mathrm c}\|_2^2=c^2\|d_A\|_2^2.
\tag{12}
\]

Every observable which depends only on the residual Fourier powers after dividing by the residual source energy is therefore **exactly complement-invariant**, not merely asymptotically close.

Equation (9) is not an arbitrary control chosen after seeing the spectrum. If `kw(x)` is interpreted as the smooth model's expected occupancy of a binary support at site `x`, then `1-kw(x)` is exactly the complementary expected occupancy; division by `m=q-k` normalizes that complementary mass.

## 3. The PC-330 Li-grid has a genuine complemented probability for large `q`

Now specialize to PC-330. Let `q` be prime, let `P_q\subset Z/qZ` be the canonical prime source set, and write

\[
R_q:=|P_q|=\pi(q),
\qquad
p_q=\frac{1_{P_q}}{R_q}.
\tag{13}
\]

PC-330 defines the Li-grid probability `w_q` by projecting the normalized logarithmic-integral measure on `[2/q,1]` to the nearest denominator-`q` grid point. In the unscaled coordinate `x=qt`, let `I_{q,j}` be the raw mass of the Voronoi cell assigned to the `j`th grid point,

\[
I_{q,j}
:=\int_{J_{q,j}}\frac{dx}{\log x},
\qquad
A_q:=\int_2^q\frac{dx}{\log x},
\qquad
w_q(j)=\frac{I_{q,j}}{A_q}.
\tag{14}
\]

Every cell `J_{q,j}` has length at most one. More importantly there is a conductor-independent constant `\eta<1` with

\[
\sup_{q,j} I_{q,j}\le\eta.
\tag{15}
\]

Indeed, the first cell beginning at `2` has length at most `1/2`, hence mass at most `1/(2\log2)<1`; the only possible full cell intersecting `(2,e)` is contained in `[5/2,7/2]`, on which convexity of `1/\log x` gives a trapezoidal upper bound below `1`; every later full cell starts above `e` and therefore has integral strictly below its length, with a uniform margin already from the first such cell. Endpoint cells are shorter. Thus a fixed `\eta<1` exists.

By the prime number theorem,

\[
\frac{A_q}{R_q}\longrightarrow1.
\tag{16}
\]

Combining (15) and (16), for all sufficiently large prime `q`,

\[
I_{q,j}<\frac{A_q}{R_q}
\qquad\text{for every }j,
\tag{17}
\]

or equivalently

\[
R_q w_q(j)<1.
\tag{18}
\]

Therefore the complementary Li occupancy

\[
\boxed{
w_q^{\mathrm c}(j)
:=\frac{1-R_qw_q(j)}{q-R_q}
}
\tag{19}
\]

is a bona fide probability vector for all sufficiently large `q`. It is the normalized smooth occupancy of the non-prime complement predicted by the same Li-grid model.

Let

\[
p_q^{\mathrm c}:=
\frac{1_{(Z/qZ)\setminus P_q}}{q-R_q},
\qquad
c_q:=\frac{R_q}{q-R_q}.
\tag{20}
\]

For the PC-330 residual and its complemented counterpart,

\[
d_q:=p_q-w_q,
\qquad
d_q^{\mathrm c}:=p_q^{\mathrm c}-w_q^{\mathrm c},
\tag{21}
\]

(11) gives the exact identity

\[
\boxed{
d_q^{\mathrm c}=-c_qd_q.
}
\tag{22}
\]

No asymptotic number-theory estimate enters (22); PNT is used only to guarantee eventually that the natural complementary baseline (19) is nonnegative.

## 4. PC-330--PC-333 normalized observables are exactly matched

Use the PC-330 notation

\[
e_q(h):=\widehat d_q(h),
\qquad
\mu_q^{\mathrm{res}}:=\|d_q\|_2^2
=\frac1q\sum_{h\ne0}|e_q(h)|^2.
\tag{23}
\]

For the complemented residual, (22) gives

\[
e_q^{\mathrm c}(h)=-c_qe_q(h),
\qquad
\mu_q^{\mathrm c}=c_q^2\mu_q^{\mathrm{res}}.
\tag{24}
\]

Consequently, frequency by frequency,

\[
\boxed{
\frac{|e_q^{\mathrm c}(h)|^2}{\mu_q^{\mathrm c}}
=
\frac{|e_q(h)|^2}{\mu_q^{\mathrm{res}}}.
}
\tag{25}
\]

This immediately propagates through the scalar branch:

- every normalized band energy `E_q(H)/\mu_q^{res}` from PC-332/PC-333 is identical for all `H`;
- every dyadic low-frequency profile `\Gamma_q(H)` of PC-332 is identical;
- every Fejer-weighted energy is identical;
- from the exact PC-333 window identity, every normalized cyclic variance `M_q(L)/\mu_q^{res}` is identical for all `L`.

The same cancellation occurs for the two-level Green-Hardy normalization. If conductors `q,r` are both complemented, then the PC-330 Green kernel

\[
X^{\mathrm{res}}_{q,r}(k,l)
=\frac{e_q(k)e_r(l)}{k+l}
\tag{26}
\]

is multiplied by the positive scalar `c_qc_r`, while its canonical Hilbert-band scale

\[
\sqrt{\mu_q^{\mathrm{res}}\mu_r^{\mathrm{res}}}
\tag{27}
\]

is multiplied by exactly the same scalar. Hence the **source-normalized Green operator itself**, not merely one band statistic, is unchanged after identifying the two constructions by this normalization. All normalized spectral data derived from that operator, including the PC-331 Hardy-energy ratios, therefore agree exactly.

This is the binary matched control that PC-325 did not supply. At every sufficiently large prime conductor, the canonical prime support and its literal support complement, paired with the same smooth model through complementary occupancy, produce identical data throughout the current normalized magnitude/autocorrelation Green-Hardy branch.

## 5. Prior-art and novelty audit

The algebra behind (3)--(12) is classical Fourier/autocorrelation theory. Complement relations for lattice subsets and their autocorrelation/diffraction are standard; a nearby explicit reference is Michael Baake, *Diffraction of Weighted Lattice Subsets*, Canadian Mathematical Bulletin 45 (2002), 483--498, DOI `10.4153/CMB-2002-050-2`. Modern finite-alphabet phase retrieval likewise treats equality of Fourier magnitudes through homometric/difference-set data; see Tamir Bendory, Dan Edidin, and Ivan Gonzalez, *Finite alphabet phase retrieval*, Applied and Computational Harmonic Analysis 66 (2023), 151--160, DOI `10.1016/j.acha.2023.04.005`, arXiv `2301.10647`.

No claim is made that support complementation, Fourier-power invariance after centering/normalizing, homometry, or phase retrieval is new. The exact identities above are self-contained and do not require either reference as a load-bearing theorem, so no new durable literature dependency is introduced into `SOURCES.md`.

The project-local result is narrower and sharper: **the finite-alphabet escape explicitly left open by PC-325 fails for the particular normalized Li-subtracted source and Green-Hardy observables developed in PC-330--PC-333.** The matched control remains binary, the smooth profile is complemented by the same occupancy model rather than discarded, and the entire normalized residual power profile agrees exactly.

## 6. Boundary

This does **not** say that prime support and non-prime support are arithmetically equivalent, nor that unnormalized observables cannot distinguish them. Equation (22) contains the scale factor `c_q`; any invariant which deliberately retains that absolute asymmetric amplitude sees the difference. The result only applies where the current branch divides out the source/Hilbert scale or otherwise factors through normalized magnitude/autocorrelation data.

It also does not close the phase-sensitive routes of PC-303--PC-305. Odd-order oriented polyspectra can detect the sign/phase change in (22), and those findings already establish that sufficiently rich phase-sensitive tensors can reconstruct the finite source up to the expected symmetries. Nor does PC-334 rule out a new cross-level construction that couples the original prime and smooth sources nonseparably before the complement scaling can be quotiented out.

What it does rule out is the remaining hope that restricting the PC-325 matched-control test to literal binary supports rescues the **normalized magnitude-only Green-Hardy branch**. It does not: the support complement is an exact finite-alphabet control even after the full PC-330 smooth subtraction and through the PC-331--PC-333 normalizations. Any surviving Prime-Circle mechanism must retain information discarded by this complement quotient, or produce a genuinely new relation to zeta zeros rather than another normalized autocorrelation statistic.

## Audit tests

The claim fails if any of the following finite identities fails: direct substitution must give (3); (9) must have total mass one and imply (11); for the PC-330 Li grid, (15)--(18) must make (19) nonnegative for all sufficiently large prime conductors; Fourier transformation must give (24); and every normalization claimed in Section 4 must cancel the scalar factors exactly. A counterexample to any one of these checks refutes the corresponding part of the finding.

Passing these checks establishes only the matched-control obstruction above. It does not establish a zeta functional equation, a critical-line theorem, an RH criterion, or a no-go for phase-sensitive/nonseparable Prime-Circle operators.