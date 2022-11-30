// pages/posts/[id].js
import { useRouter } from 'next/router';

const slug = () => {
    const router = useRouter()
    const query = router.query;

    return (
        <div>slug - {query}</div>
    )
}

export default slug