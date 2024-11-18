#include <iostream>
#include <memory>

struct MemoryTracker {
    static size_t total_allocated;

    static void* allocate(size_t size) {
        total_allocated += size;
        return std::malloc(size);
    }

    static void deallocate(void* ptr, size_t size) {
        total_allocated -= size;
        std::free(ptr);
    }
};

size_t MemoryTracker::total_allocated = 0;

template <typename T>
struct TrackingAllocator {
    using value_type = T;

    T* allocate(size_t n) {
        size_t bytes = n * sizeof(T);
        return static_cast<T*>(MemoryTracker::allocate(bytes));
    }

    void deallocate(T* p, size_t n) {
        size_t bytes = n * sizeof(T);
        MemoryTracker::deallocate(p, bytes);
    }
};
